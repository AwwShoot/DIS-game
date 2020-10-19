
from logwriter import mainwriter
import pygame
from pygame import rect

class Snake:

    def __init__(self, coordinates):
        """

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


#putting the first block of snake here





    """
    direction will be a string that is either 'up', 'down', 'left' or 'right' representing which way the snake moves
    This function will modify the coordinates of the snake appropriately 
    """
    def move(self, direction):
        # coordinates[2] represents the current head piece before a new head piece is made
        if direction=="up":
            mainwriter.write("moving up from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] - 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] - 1)*64, 64, 64))
            self.last_move="up"
        if direction=="down":
            mainwriter.write("moving down from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] + 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] + 1)*64, 64, 64))
            self.last_move="down"
        if direction=="left":
            mainwriter.write("moving left from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]-1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]-1)*64, self.coordinates[2][1]*64, 64, 64))
            self.last_move="left"
        if direction=="right":
            mainwriter.write("moving right from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]+1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]+1)*64, self.coordinates[2][1]*64, 64, 64))
            self.last_move="right"




    def check_collision(self, opponent, boundaries, player):
        """
        NOTE: this does not check for collision w/ self. runs off the basis that the snake is 4 segments long and therefore cannot self-collide.
        :param opponent: list of collision boxes of the opponent snake.
        :param boundaries: list of collision boxes of the boundaries
        :param player: 1 if player 1, 2 if player 2 ect. determines the respawn X coords.
        :return:
        """
        head=self.collision_boxes[-1]
        if head.collidelist(opponent)!=-1 or head.collidelist(boundaries)!=-1:
            mainwriter.write("snake? snaaaaake!")
            self.coordinates=[[0+(player*15-15),0], [0+(player*15-15),1], [0+(player*15-15),2], [0+(player*15-15),3]]
            self.last_move=""
            self.collision_boxes = []
            for i in self.coordinates:
                self.collision_boxes.append(rect.Rect(i[0] * 64, i[1] * 64, 64, 64))
        for i in self.coordinates:
            if i[0]<0 or i[0]>15 or i[1]<0 or i[1]>7:
                mainwriter.write("snake out of bounds")
                self.coordinates = [[0 + (player * 7 - 7), 0], [0 + (player * 7 - 7), 1], [0 + (player * 7 - 7), 2], [0 + (player * 7 - 7), 3]]
                self.last_move=""
                self.collision_boxes = []
                for i in self.coordinates:
                    self.collision_boxes.append(rect.Rect(i[0] * 64, i[1] * 64, 64, 64))




    def grow(self):
        self.coordinates.insert(0, self.coordinates[0])
        self.collision_boxes.insert(0, self.collision_boxes[0])