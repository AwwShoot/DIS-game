#I have no clue why these imports are showing up as errors, the code runs fine though.
from logwriter import mainwriter
import pygame

#this makes the audio work
pygame.init()

bong = pygame.mixer.Sound(r'src/assets/pongsoundeffect.wav')
bam = pygame.mixer.Sound(r'src/assets/bam.wav')

class Ball:
    def __init__(self, coordinates, velocity):
        """

        :param coordinates: a single coordinate pair in float form indicating the starting position of the ball. top left corner.
        :param velocity: a list of two float values determining the change in X and Y coordinates per frame*
        * IDK yet how "fast" this will run, so these may change in scale over development
        """
        self.coordinates=coordinates
        self.base_x_vel=velocity[0]+0
        self.base_y_vel=velocity[1]+0
        self.base_velocity=[self.base_x_vel, self.base_y_vel]
        self.velocity=velocity
        # Collision boxes is a dictionary of four rectangles on the edges of the object for determining collision sides.
        # Ordered as top, bottom, left, right.
        # The following indent here has no program effect, it's just a trick to make long lines readable.
        self.collision_boxes = {"left": pygame.rect.Rect(self.coordinates[0], self.coordinates[1]+16, 16, 32), "right": pygame.rect.Rect(self.coordinates[0]+48, self.coordinates[1]+16, 16, 32),
                                "top": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1], 32, 16), "bottom": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1]+48, 32, 16)}
        self.sprite_box = pygame.rect.Rect(self.coordinates[0], self.coordinates[1], 64, 64)
        # A list of recent collision checks and whether or not the ball bounced. If there are three Trues in a row, it reset's the ball's position.
        self.recent_bounces=[False, False, False, False, False]
        self.last_hit=""


    def move(self):

        #This will be called every "frame" of the game, whatever that may be
        if(self.recent_bounces[0] and self.recent_bounces[1] and self.recent_bounces[2]):
            self.set_position([512, 256], False)
        if(self.coordinates[0]>1100 or self.coordinates[0]<-100 or self.coordinates[1]>612 or self.coordinates[1]<-100):
            self.set_position([512, 256], False)
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]
        self.sprite_box.move(self.velocity[0], self.velocity[1])
        for box in self.collision_boxes:
            self.collision_boxes[box].move_ip(self.velocity[0], self.velocity[1])
        self.sprite_box.move_ip(self.velocity[0], self.velocity[1])



    def bounce(self, horizontal):
        """
        :param horizontal: boolean. true if the ball bounces horizontally off a vertical surface(e.g. the side of a snake)


        """

        if horizontal:
            mainwriter.write("Bouncing horizontally: \n")
            self.velocity[0]= 0 - self.velocity[0]
            self.manage_speed()
            pygame.mixer.Sound.play(bong)
            pygame.mixer.music.stop()
        else:
            mainwriter.write("Bouncing vertically: \n")
            self.velocity[1]= 0 - self.velocity[1]
            self.manage_speed()
            pygame.mixer.Sound.play(bong)
            pygame.mixer.music.stop()


    def set_position(self, coordinates, keep_vel):
        """

        :param coordinates: a list coordinate pair where the ball should respawn
        :param keep_vel: a boolean. If True, velocity is kept the same, otherwise it is set to default
        :return:
        """
        mainwriter.write("setting ball's position \n")
        self.collision_boxes["top"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["bottom"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["left"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["right"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.sprite_box.move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.coordinates = coordinates
        if not keep_vel:
            mainwriter.write(f"resetting the velocity to {self.base_velocity[0]}, {self.base_velocity[1]} \n")
            self.velocity=self.base_velocity

    def set_velocity(self, velocity):
        self.velocity=velocity

    def check_collision_box(self, box, snake_one, snake_two, boundaries, tetronimos):
        """
`
        :param box: a string of "top", "bottom", "left", or "right", which relates to a collision box in the dictionary of collision boxes.
        :param snake_one: the list of collision boxes from a snake object
        :param snake_two: ditto
        :param boundaries: a list of rects for any other boundaries such as the edge of the screen.
        :return: true if it bounces. note that the return statement ends the function early, so it doesn't consider multiple collisions
        I use the return statement to end the program early as well.
        This also updates the recent_bounces list with whether or not the ball bounces
        sets last_hit equal to p1 or p2 if player one or player two just collided with the ball
        """
        if self.collision_boxes[box].collidelist(snake_one) !=-1:
            mainwriter.write(f"{box} collided with player one\n")
            return True
        elif self.collision_boxes[box].collidelist(snake_two) !=-1:
            mainwriter.write(f"{box} collided with player two\n")
            return True
        elif self.collision_boxes[box].collidelist(boundaries)!= -1:
            mainwriter.write(f"{box} collided with the boundaries\n")
            return True
        elif self.collision_boxes[box].collidelist(tetronimos)!= -1:
            mainwriter.write(f"{box} collided with the boundaries\n")
            return True


        self.recent_bounces.pop(0)
        self.recent_bounces.append(False)
        return False




    def check_collision(self, snake_one, snake_two, boundaries, tetronimos):
        """
        this will be called by the main program during the game loop
        It checks through the boxes prioritizing horizontal bounces first
        :param tetronimos: a list of collision boxes from tetronimos. premade in main.py
        :param snake_one: a list of collision boxes from a snake object
        :param snake_two: ditto
        :param boundaries: a list of collision boxes for any other boundaries such as the edge of the screen.
        :return: true if it bounces.
        """

        for box in self.collision_boxes:
            if len(snake_one)==4:
                if self.collision_boxes[box].colliderect(snake_one[3]) and (box=="left" or box=="right"):
                    if box=="left":
                        self.set_position([self.coordinates[0]+64, self.coordinates[1]], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                    else:
                        self.set_position([self.coordinates[0]-64, self.coordinates[1]], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                if self.collision_boxes[box].colliderect(snake_one[3]) and (box=="top" or box=="bottom"):
                    self.velocity[1] = self.base_velocity[1] * 2
                    if box=="top":
                        self.set_position([self.coordinates[0], self.coordinates[1]+64], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                    else:
                        self.set_position([self.coordinates[0], self.coordinates[1] - 64], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()

                    self.velocity[0] = self.base_velocity[0] * 2

            if len(snake_two) == 4:
                if self.collision_boxes[box].colliderect(snake_two[3]) and (box=="left" or box=="right"):
                    if box=="left":
                        self.set_position([self.coordinates[0]+64, self.coordinates[1]], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                    else:
                        self.set_position([self.coordinates[0]-64, self.coordinates[1]], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                if self.collision_boxes[box].colliderect(snake_two[3]) and (box=="top" or box=="bottom"):
                    self.velocity[1] = self.base_velocity[1] * 2
                    if box=="top":
                        self.set_position([self.coordinates[0], self.coordinates[1]+64], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()
                    else:
                        self.set_position([self.coordinates[0], self.coordinates[1] - 64], True)
                        pygame.mixer.Sound.play(bam)
                        pygame.mixer.music.stop()

                    self.velocity[0] = self.base_velocity[0] * 2



        if self.check_collision_box("top", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(False)
            self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("bottom", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(False)
            self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("left", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(True)
            self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("right", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(True)
            self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True


    def try_shunt(self, snake_one, snake_two, boundaries, tetronimos):
        """
        Will check if the ball is stuck colliding against the same object over and over.
        :return: The ball will be forced out of whatever object it is stuck in.
        """
        top_colliding=self.check_collision_box("top", snake_one, snake_two, boundaries, tetronimos)
        bottom_colliding=self.check_collision_box("bottom", snake_one, snake_two, boundaries, tetronimos)
        left_colliding=self.check_collision_box("left", snake_one, snake_two, boundaries, tetronimos)
        right_colliding=self.check_collision_box("right", snake_one, snake_two, boundaries, tetronimos)
        total_collisions= (1 if top_colliding else 0) + (1 if bottom_colliding else 0) + (1 if left_colliding else 0) + (1 if right_colliding else 0)
        if total_collisions==4:
            self.set_position([512, 256], False)
        # Double asterisks (**) expnonentiate the value rather than multiply (like the ^ on a calculator).
        # For the math of this shunting, basically the deeper into the object you are, the further you are pushed out. 8 pixels for one collision, 16 for two and 32 for three
        if top_colliding:
            self.set_position([self.coordinates[0], self.coordinates[1] + 4 * (1+2 ** total_collisions)], True)
        if bottom_colliding:
            self.set_position([self.coordinates[0], self.coordinates[1] - 4 * (1+2 ** total_collisions)], True)
        if left_colliding:
            self.set_position([self.coordinates[0] + 4 * (1+2 ** total_collisions), self.coordinates[1]], True)
        if right_colliding:
            self.set_position([self.coordinates[0] - 4 * (1+2 ** total_collisions), self.coordinates[1]], True)


    def score(self):
        """
        Run this to check if a player has scored.
        :return: 0 if no score, 1 if P1 scores (ball in right goal) 2 if P2 scores (ball in left goal)
        """
        if self.coordinates[0]+32>960:
            self.set_position([512, 256], False)
            return 1
        if self.coordinates[0]+32<64:
            self.set_position([512, 256], False)
            return 2
        return 0

    def manage_speed(self):
        if self.velocity[1] < self.base_velocity[1] and self.velocity[1] > 0 - self.base_velocity[1]:
            mainwriter.write(f'verticle speed is too low, ({self.velocity[1]}), resetting speed  \n')
            self.velocity[1] = self.base_velocity[1]

        if self.velocity[1] > self.base_velocity[1]:
            mainwriter.write(f"ball slowing down. verticle speed was {self.velocity[1]}  ")
            self.velocity[1] -= 1
            mainwriter.write(f"now {self.velocity[1]} \n")

        if self.velocity[1] < 0 - self.base_velocity[1]:
            mainwriter.write(f"ball slowing down. verticle speed was {self.velocity[1]}  ")
            self.velocity[1] += 1
            mainwriter.write(f"now {self.velocity[1]} \n")

        # Horizontal speed
        if self.velocity[0] < self.base_velocity[0] and self.velocity[0] > 0 - self.base_velocity[1]:
            mainwriter.write(f'horizontal speed is too low, ({self.velocity[0]}), resetting speed  \n')
            self.velocity[0] = self.base_velocity[0]

        if self.velocity[0] > self.base_velocity[0]:
            mainwriter.write(f"ball slowing down. horizontal speed was {self.velocity[0]}  ")
            self.velocity[0] -= 1
            mainwriter.write(f"now {self.velocity[0]} \n")

        if self.velocity[0] < 0 - self.base_velocity[0]:
            mainwriter.write(f"ball slowing down. horizontal speed was {self.velocity[0]}  ")
            self.velocity[0] += 1
            mainwriter.write(f"now {self.velocity[0]} \n")


