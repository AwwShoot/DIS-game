import logwriter
from logwriter import log

class Ball():
    def __init__(self, coordinates, velocity):
        """

        :param coordinates: a single coordinate pair in float form indicating the starting position of the ball.
        :param velocity: a list of two float values determining the change in X and Y coordinates per frame*
        * IDK yet how "fast" this will run, so these may change in scale over development
        """
        self.coordinates=coordinates
        self.veloctiy=velocity

    def move(self):
        self.coordinates[0] += self.veloctiy[0]
        self.coordinates[1] += self.veloctiy[1]

    def bounce(self, horizontal, verticle):
        """
        :param horizontal: boolean. true if the ball bounces horizontally off a vertical surface(e.g. the side of a snake)
        :param verticle: boolean. true if the ball bounces vertically off a horizontal surface (e.g. floor or ceiling of the game)

        """
        if(horizontal):
            self.veloctiy[0]=0-self.veloctiy[0]
        if(verticle):
            self.veloctiy[1]=0-self.veloctiy[1]