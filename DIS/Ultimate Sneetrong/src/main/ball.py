#I have no clue why these imports are showing up as errors, the code runs fine though.
from logwriter import mainwriter
import pygame

#this makes the audio work
pygame.init()

bong = pygame.mixer.Sound(mainwriter.resource_path("src/assets/pongsoundeffect.wav"))
bam = pygame.mixer.Sound(mainwriter.resource_path('src/assets/bam.wav'))

class Ball:
    def __init__(self, coordinates, velocity):
        """

        :param coordinates: a single coordinate pair in float form indicating the starting position of the ball. top left corner.
        :param velocity: a list of two int values determining the change in X and Y coordinates per frame*
        * IDK yet how "fast" this will run, so these may change in scale over development
        """
        self.coordinates=coordinates
        self.base_x=6
        self.base_y=3

        self.velocity=velocity
        # Collision boxes is a dictionary of four rectangles on the edges of the object for determining collision sides.
        # Ordered as left right top bottom.
        # The following indent here has no program effect, it's just a trick to make long lines readable.
        self.collision_boxes = {"left": pygame.rect.Rect(self.coordinates[0], self.coordinates[1]+16, 32, 32), "right": pygame.rect.Rect(self.coordinates[0]+32, self.coordinates[1]+16, 32, 32),
                                "top": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1], 32, 32), "bottom": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1]+32, 32, 32)}
        self.sprite_box = pygame.rect.Rect(self.coordinates[0], self.coordinates[1], 64, 64)
        # A list of recent collision checks and whether or not the ball bounced. If there are three Trues in a row, it resets the ball's position.
        self.recent_bounces=[False, False, False]
        self.last_hit=""
        # Counts down to 0 when respawning instead of moving.
        self.respawn_timer=0
        # When false: Do not check collision. Ball is respawning and should not be touched.
        self.colliding=True


    def move(self):
        if self.respawn_timer>0:
            self.respawn()

        #This will be called every "frame" of the game, whatever that may be
        if(self.recent_bounces[0] and self.recent_bounces[1] and self.recent_bounces[2]):
            self.destroy()
        if(self.coordinates[0]>1100 or self.coordinates[0]<-100 or self.coordinates[1]>612 or self.coordinates[1]<-100):
            self.destroy()
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

        else:
            mainwriter.write("Bouncing vertically: \n")
            self.velocity[1]= 0 - self.velocity[1]
        self.move()
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
        if not keep_vel: #This is for if the ball is getting out of bounds or collision issues due to it's speed.
            mainwriter.write(f"resetting the velocity to {self.base_x}, {self.base_y} \n") #This output is seen when verticle velocity=0, and says that base_velocity[1]=0
            self.velocity[0]=self.base_x
            self.velocity[1]=self.base_y



    def check_collision_box(self, box, snake_one, snake_two, boundaries, tetronimos):
        """
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
        It checks through the boxes prioritizing verticle bounces first
        :param tetronimos: a list of collision boxes from tetronimos. premade in main.py
        :param snake_one: a list of collision boxes from a snake object
        :param snake_two: ditto
        :param boundaries: a list of collision boxes for any other boundaries such as the edge of the screen.
        :return: true if it bounces.
        """

        for box in self.collision_boxes:
            # Should not crash if a snake is missing. Checks that the ball collision is with a head.
            if (len(snake_one)==4 and self.collision_boxes[box].colliderect(snake_one[3])):
                changeX = snake_one[3].x-snake_one[2].x
                changeY = snake_one[3].y-snake_one[2].y
                if changeX!=0:
                    self.set_position([self.coordinates[0] +changeX, self.coordinates[1]], True)
                    pygame.mixer.Sound.play(bam)
                    pygame.mixer.music.stop()
                    self.velocity[0] = changeX/2
                else:
                    self.set_position([self.coordinates[0], self.coordinates[1]+changeY], True)
                    pygame.mixer.Sound.play(bam)
                    pygame.mixer.music.stop()
                    self.velocity[1] = changeY / 2
            elif (len(snake_two) == 4 and self.collision_boxes[box].colliderect(snake_two[3])):
                changeX = snake_two[3].x - snake_two[2].x
                changeY = snake_two[3].y - snake_two[2].y
                if changeX != 0:
                    self.set_position([self.coordinates[0] + changeX, self.coordinates[1]], True)
                    pygame.mixer.Sound.play(bam)
                    pygame.mixer.music.stop()
                    self.velocity[0] = changeX / 2
                else:
                    self.set_position([self.coordinates[0], self.coordinates[1] + changeY], True)
                    pygame.mixer.Sound.play(bam)
                    pygame.mixer.music.stop()
                    self.velocity[1] = changeY / 2


        if self.check_collision_box("top", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(False)
            #self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("bottom", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(False)
            #self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("left", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(True)
            #self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
            return True
        elif self.check_collision_box("right", snake_one, snake_two, boundaries, tetronimos):
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            self.bounce(True)
            #self.try_shunt(snake_one, snake_two, boundaries, tetronimos)
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
            self.destroy()
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
            self.destroy()
            return 1
        if self.coordinates[0]+32<64:
            self.destroy()
            return 2
        return 0

    def manage_speed(self):
        """
        Called whenever the ball bounces to slow down the ball if it's too fast or fix it if it gets too low.
        """
        if self.velocity[1] < self.base_y and self.velocity[1] > 0 - self.base_y: #Resets verticle velocity if it is lower than the base velocity and higher than the negative of the base
            mainwriter.write(f'verticle speed is too low, ({self.velocity[1]}), resetting speed  \n') #mainwriter is a seperate class using the I/0 features to output info to a log file for debugging.
            self.velocity[1] = self.base_y

        if self.velocity[1] > self.base_y:
            mainwriter.write(f"ball slowing down. verticle speed was {self.velocity[1]}  ")
            self.velocity[1] -= 1
            mainwriter.write(f"now {self.velocity[1]} \n")

        elif self.velocity[1] < 0 - self.base_y:
            mainwriter.write(f"ball slowing down. verticle speed was {self.velocity[1]}  ")
            self.velocity[1] += 1
            mainwriter.write(f"now {self.velocity[1]} \n")

        # Horizontal speed
        if self.velocity[0] < self.base_x and self.velocity[0] > 0 - self.base_x: #Same as the hashtag marked line for verticle velocity.
            mainwriter.write(f'horizontal speed is too low, ({self.velocity[0]}), resetting speed  \n') #These outputs are never seen in the output log.
            self.velocity[0] = self.base_x

        if self.velocity[0] > self.base_x:
            mainwriter.write(f"ball slowing down. horizontal speed was {self.velocity[0]}  ")
            self.velocity[0] -= 1
            mainwriter.write(f"now {self.velocity[0]} \n")

        elif self.velocity[0] < 0 - self.base_x:
            mainwriter.write(f"ball slowing down. horizontal speed was {self.velocity[0]}  ")
            self.velocity[0] += 1
            mainwriter.write(f"now {self.velocity[0]} \n")


    # Both of these functions are entirely self-contained. Tinker around with them as much as you need to get the animation looking cool and good :]
    def destroy(self):
        """
        Sets respawn time to the appropriate number of ticks and resets the ball for respawning.
        Called when the ball would despawn on older versions of the code
        """
        self.set_position([512, 64], False)
        self.respawn_timer=1
        self.colliding=False

    def respawn(self):
        """
        decreases respawn timer and potentially plays the respawn animation.
        Called instead of move() whenever respawn_timer>0
        """
        if self.respawn_timer<=0:
            self.colliding=True
            self.respawn_timer=0
        else:
            self.respawn_timer-=1
            #Play the next frame here(?)

