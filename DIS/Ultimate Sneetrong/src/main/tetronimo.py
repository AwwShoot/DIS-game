from logwriter import mainwriter
import pygame
from pygame import rect

class Tetronimo:
    next_ID=0
    def __init__(self, coordinates):
        """

        :param coordinates: a list of coordinate pairs for the piece.
        Tetronimo.next_ID is a static variable because it is instantiated without a self. prepended and is instantiated in the class but outside of the methods.
        This means that Tetronimo.next_ID will be the same value to each tetronimo object, so the following code can give each tetronimo a unique ID number.
        The ID number is to make sure a tetronimo doesn't check if it collides with itself (which it does since it is itself).
        the boolean "active" will tell main.py if it is an active tetronimo or if it has been removed somehow.
        """
        self.ID=Tetronimo.next_ID
        Tetronimo.next_ID+=1
        self.active=True

        self.coordinates=coordinates
        self.collision_boxes=[]
        for pair in coordinates:
            # boxes are an extra pixel tall downwards. This is so they can check collision immediately below them without moving or other funky stuff.
            self.collision_boxes.append(rect.Rect(pair[0]*64, pair[1]*64, 64, 65))

    def move(self, boundaries, tetronimos):
        """

        :param boundaries: list of collision boxes for boundaries
        :param tetronimos: list of tetronimos present in the world.
        checks if a tetronimo can move first before dropping it down.
        """
        for box in self.collision_boxes:
            if box.collidelist(boundaries) == -1:
                for tetron in tetronimos:
                    if tetron.ID!=self.ID:
                        for box in self.collision_boxes:
                            if box.collidelist(tetron.collision_boxes) == -1:
                                for box in self.collision_boxes:
                                    box.move_ip(0, 64)

    @staticmethod
    def check_lines(tetronimos):
        """

        :param tetronimos: a list of active tetronimo objects
        :return: the Y coordinate of the line completed. returns -1 if no line is completed
        """
        tester=rect.Rect(0, 504, 8, 8)
        for y in range(8):
            for x in range(16):
                if tester.collidelist(tetronimos):
                    tester.move_ip(64, 0)
                else:
                    break
                if x==15:
                    return 7-y
            tester.move_ip(-1024,64)
        return -1

    def remove(self):
        """
        makes a tetronimo inactive and uncollidable. Inactive tetronimos should be removed from the list of tetronimos present in-game and will eventually be deleted by
        python's automated memory cleanup.
        """
        self.active=False
        self.coordinates=[[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        self.collision_boxes=[]