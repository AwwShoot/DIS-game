
from logwriter import mainwriter
import pygame
from pygame import rect
from tetronimo import Tetronimo

class Snake:

    def __init__(self, coordinates, player):
        """
        :param player: 1 or 2, for player 1 or two.
        :param coordinates: a list of four coordinate pairs representing the position of each segment of the body.
        The first pair represents the tail while the last represents the head
        """
        self.coordinates=coordinates
        self.collision_boxes=[]
        for pair in coordinates:
            self.collision_boxes.append(rect.Rect(pair[0]*64, pair[1]*64, 64, 64))
            # coordinates are based off a 64x64 pixel grid so each rect object will be instantiated at 64 pixels times the grid coordinate.
        #string of "up", "down", "left", or "right", which is the last direction the snake moved in. This is used to keep the snake from instantly doubling back on itself.
        self.last_move=""
        self.player=player
        self.removed=False








    """
    direction will be a string that is either 'up', 'down', 'left' or 'right' representing which way the snake moves
    This function will modify the coordinates of the snake appropriately 
    """
    def move(self, direction):
        # coordinates[2] represents the current head piece before a new head piece is made
        if direction=="up":

            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] - 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] - 1)*64, 64, 64))
            self.last_move="up"
        if direction=="down":

            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] + 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] + 1)*64, 64, 64))
            self.last_move="down"
        if direction=="left":

            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]-1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]-1)*64, self.coordinates[2][1]*64, 64, 64))
            self.last_move="left"
        if direction=="right":

            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]+1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]+1)*64, self.coordinates[2][1]*64, 64, 64))
            self.last_move="right"



    def remove(self):
        """
        "deletes" the snake, so it can be respawned at a later time.
        """

        self.last_move = ""
        self.collision_boxes = []
        self.removed=True


    def replace(self):
        """
        replaces a removed snake.
        """
        if self.removed:
            self.coordinates = [[0 + (self.player * 15 - 15), 0], [0 + (self.player * 15 - 15), 1],
                                [0 + (self.player * 15 - 15), 2], [0 + (self.player * 15 - 15), 3]]
            for i in self.coordinates:
                self.collision_boxes.append(rect.Rect(i[0] * 64, i[1] * 64, 64, 64))
            self.removed=False


    def check_collision(self, opponent, boundaries, tetronimos):
        """
        NOTE: this does not check for collision w/ self. runs off the basis that the snake is 4 segments long and therefore cannot self-collide.
        :param opponent: list of collision boxes of the opponent snake.
        :param boundaries: list of collision boxes of the boundaries
        :param player: 1 if player 1, 2 if player 2 ect. determines the respawn X coords.
        :return: True if the snake collides and is removed. False otherwise.
        """
        head=self.collision_boxes[-1]
        if head.collidelist(opponent)!=-1 or head.collidelist(boundaries)!=-1:
            mainwriter.write("snake? snaaaaake!\n")
            self.remove()
            return True

        for piece in tetronimos:
            if head.collidelist(piece.collision_boxes)!=-1:
                piece.remove()
                mainwriter.write("snake? snaaaaake!\n")
                self.remove()
                return True

        for i in self.coordinates:
            if i[0]<0 or i[0]>15 or i[1]<0 or i[1]>7:
                mainwriter.write("snake out of bounds\n")
                self.remove()
                return True
        return False




    def tetrify(self):
        """
        :param: player is the number of the player. if not 1 or 2, the function does nothing.
        Creates a tetronimo at the position and status of the snake.
        :return: the tetronimo created.
        """


        chunk=Tetronimo(self.coordinates, self.player)
        self.remove()
        return chunk



