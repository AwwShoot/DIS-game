
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
        for i in coordinates:
            self.collision_boxes.append(rect.Rect(i[0]*64, i[1]*64, 64, 64))
            # coordinates are based off a 64x64 pixel grid so each rect object will be instantiated at 64 pixels times the grid coordinate.

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
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] + 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] + 1)*64, 64, 64))
            mainwriter.write_coordinates(self.coordinates)

        if direction=="down":
            mainwriter.write("moving down from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0], self.coordinates[2][1] - 1])
            self.collision_boxes.append(rect.Rect(self.coordinates[2][0]*64, (self.coordinates[2][1] - 1)*64, 64, 64))
            mainwriter.write_coordinates(self.coordinates)
        if direction=="left":
            mainwriter.write("moving left from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]-1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]-1)*64, self.coordinates[2][1]*64, 64, 64))
            mainwriter.write_coordinates(self.coordinates)
        if direction=="right":
            mainwriter.write("moving right from: ")
            mainwriter.write_coordinates(self.coordinates)
            self.coordinates.pop(0)
            self.collision_boxes.pop(0)
            self.coordinates.append([self.coordinates[2][0]+1, self.coordinates[2][1]])
            self.collision_boxes.append(rect.Rect((self.coordinates[2][0]+1)*64, self.coordinates[2][1]*64, 64, 64))
            mainwriter.write_coordinates(self.coordinates)


    def get_position(self):
        return self.coordinates

    def grow(self):
        self.coordinates.insert(0, self.coordinates[0])
        self.collision_boxes.insert(0, self.collision_boxes[0])