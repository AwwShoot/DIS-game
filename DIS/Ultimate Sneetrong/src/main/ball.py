#I have no clue why these imports are showing up as errors, the code runs fine though.
from logwriter import mainwriter
import pygame

class Ball:
    def __init__(self, coordinates, velocity):
        """

        :param coordinates: a single coordinate pair in float form indicating the starting position of the ball. top left corner.
        :param velocity: a list of two float values determining the change in X and Y coordinates per frame*
        * IDK yet how "fast" this will run, so these may change in scale over development
        """
        self.coordinates=coordinates
        self.velocity=velocity
        # Collision boxes is a dictionary of four rectangles on the edges of the object for determining collision sides.
        # Ordered as top, bottom, left, right.
        # The following indent here has no program effect, it's just a trick to make long lines readable.
        self.collision_boxes = {"top": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1], 32, 16), "bottom": pygame.rect.Rect(self.coordinates[0]+16, self.coordinates[1]+48, 32, 16),
                                "left": pygame.rect.Rect(self.coordinates[0], self.coordinates[1]+16, 16, 32), "right": pygame.rect.Rect(self.coordinates[0]+48, self.coordinates[1]+16, 16, 32)}
        self.sprite_box = pygame.rect.Rect(self.coordinates[0], self.coordinates[1], 64, 64)
        # A list of recent collision checks and whether or not the ball bounced. If there are three Trues in a row, it reset's the ball's position.
        self.recent_bounces=[False, False, False]


    def move(self):

        #This will be called every "frame" of the game, whatever that may be
        if(self.recent_bounces[0] and self.recent_bounces[1] and self.recent_bounces[2]):
            self.set_position([512, 256])
        if(self.coordinates[0]>1100 or self.coordinates[0]<-100 or self.coordinates[1]>612 or self.coordinates[1]<-100):
            self.set_position([512, 256])
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
            mainwriter.write("Bouncing horizontally: ")
            mainwriter.write_position(self.coordinates)
            self.velocity[0]= 0 - self.velocity[0]
        else:
            mainwriter.write("Bouncing vertically: ")
            mainwriter.write_position(self.coordinates)
            self.velocity[1]= 0 - self.velocity[1]

    def set_position(self, coordinates):
        self.collision_boxes["top"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["bottom"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["left"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.collision_boxes["right"].move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.sprite_box.move_ip(coordinates[0]-self.coordinates[0], coordinates[1]-self.coordinates[1])
        self.coordinates = coordinates

    def set_velocity(self, velocity):
        self.velocity=velocity

    def check_collision_box(self, box, snake_one, snake_two, boundaries):
        """
`
        :param box: a string of "top", "bottom", "left", or "right", which relates to a collision box in the dictionary of collision boxes.
        :param snake_one: the list of collision boxes from a snake object
        :param snake_two: ditto
        :param boundaries: a list of rects for any other boundaries such as the edge of the screen.
        :return: true if it bounces. note that the return statement ends the function early, so it doesn't consider multiple collisions
        I use the return statement to end the program early as well.
        This also updates the recent_bounces list with whether or not the ball bounces
        """
        if self.collision_boxes[box].collidelist(snake_one) !=-1:
            mainwriter.write(f"{box} collided with player one")
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            if box=="top" or box=="bottom":
                self.bounce(False)
                return True
            else:
                self.bounce(True)
                return True
        elif self.collision_boxes[box].collidelist(snake_two) !=-1:
            mainwriter.write(f"{box} collided with player two")
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            if box=="top" or box=="bottom":
                self.bounce(False)
                return True
            else:
                self.bounce(True)
                return True
        elif self.collision_boxes[box].collidelist(boundaries)!= -1:
            mainwriter.write(f"{box} collided with the boundaries")
            self.recent_bounces.pop(0)
            self.recent_bounces.append(True)
            if box=="top" or box=="bottom":
                self.bounce(False)
                return True
            else:
                self.bounce(True)
                return True
        self.recent_bounces.pop(0)
        self.recent_bounces.append(False)
        return False




    def check_collision(self, snake_one, snake_two, boundaries):
        """
        this will be called by the main program during the game loop
        It checks through the boxes in counterclockwise order rather than top-bottom-left-right so that verticle bounces aren't weighted as heavily
        :param snake_one: a list of collision boxes from a snake object
        :param snake_two: ditto
        :param boundaries: a list of collision boxes for any other boundaries such as the edge of the screen.
        :return: true if it bounces.
        """
        if self.check_collision_box("top", snake_one, snake_two, boundaries):
            return True
        elif self.check_collision_box("left", snake_one, snake_two, boundaries):
            return True
        elif self.check_collision_box("right", snake_one, snake_two, boundaries):
            return True
        elif self.check_collision_box("bottom", snake_one, snake_two, boundaries):
            return True



