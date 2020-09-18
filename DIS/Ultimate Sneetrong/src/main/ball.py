#I have no clue why these imports are showing up as errors, the code runs fine though.
import logwriter
from logwriter import log
import pygame

class Ball():
    def __init__(self, coordinates, velocity):
        """

        :param coordinates: a single coordinate pair in float form indicating the starting position of the ball.
        :param velocity: a list of two float values determining the change in X and Y coordinates per frame*
        * IDK yet how "fast" this will run, so these may change in scale over development
        """
        self.coordinates=coordinates
        self.velocity=velocity
        # TODO: make four collision boxes one for each cardinal direction to determine where the ball is bouncing away from.
        self.collision_box = pygame.rect.Rect(self.coordinates[0], self.coordinates[1], 64, 64)


    def move(self):
        #This will be called every "frame" of the game, whatever that may be
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]
        self.collision_box.move_ip(self.velocity[0], self.velocity[1])
        logwriter.write_position(self.coordinates)
        log.write(self.collision_box.__str__())


    def bounce(self, horizontal, verticle):
        """
        :param horizontal: boolean. true if the ball bounces horizontally off a vertical surface(e.g. the side of a snake)
        :param verticle: boolean. true if the ball bounces vertically off a horizontal surface (e.g. floor or ceiling of the game)

        """
        if(horizontal):
            log.write("Bouncing horizontally: ")
            logwriter.writecoords(self.coordinates)
            self.velocity[0]= 0 - self.velocity[0]
        if(verticle):
            log.write("Bouncing vertically: ")
            logwriter.writecoords(self.coordinates)
            self.velocity[1]= 0 - self.velocity[1]

    def set_position(self, coordinates):
        self.coordinates=coordinates

    def set_velocity(self, velocity):
        self.velocity=velocity

    def check_collision(self, snake_one, snake_two, boundaries):
        #TBI
        pass
#Honestly IDK if accessor methods like these have any use in Python, I just know they were important for Java so I've plunked them in
    def get_position(self):
        return self.coordinates

    def get_velocity(self):
        return self.velocity