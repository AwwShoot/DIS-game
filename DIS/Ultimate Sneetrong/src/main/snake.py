class Snake():

    def __init__(self, coordinates):
        """

        :param coordinates: a list of four coordinate pairs representing the position of each segment of the body.
        The first pair represents the tail while the last represents the head
        """
        self.coordinates=coordinates

    """
    direction will be a string that is either 'up', 'down', 'left' or 'right' representing which way the snake moves
    This function will modify the coordinates of the snake appropriately 
    """
    def move(self, direction):
        if direction=="up":
            self.coordinates.pop(0)
            self.coordinates.append([self.coordinates[2][0],self.coordinates[2][1] + 1])
        if direction=="down":
            self.coordinates.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] - 1])
        if direction=="left":
            self.coordinates.pop(0)
            self.coordinates.append([self.coordinates[2][0]-1, self.coordinates[2][1]])
        if direction=="right":
            self.coordinates.pop(0)
            self.coordinates.append([self.coordinates[2][0]+1, self.coordinates[2][1]])


    def getcoords(self):
        return self.coordinates