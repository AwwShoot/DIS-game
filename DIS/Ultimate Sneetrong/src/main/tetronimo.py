from logwriter import mainwriter
import pygame
from pygame import rect

class Tetronimo:
    next_ID=0
    def __init__(self, coordinates, player):
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
        self.player=player

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
            if box.collidelist(boundaries) != -1:
                return

        for piece in tetronimos:
            if piece.ID!=self.ID:
                for box in self.collision_boxes:
                    if box.collidelist(piece.collision_boxes) != -1:
                        return

        for box in self.collision_boxes:
            box.move_ip(0, 64)

    @staticmethod
    def check_lines(tetronimos):
        """

        :param tetronimos: a list of active tetronimo objects
        :return: the Y coordinate of the line completed. returns -1 if no line is completed
        """
        tester=rect.Rect(1, 1, 1, 1)
        for y in range(8): # Each iteration of this loop is checking one row. Starts at the top.
            for x in range(16): #Each iteration is a specific tile.
                if tester.collidelist(tetronimos)!=-1: #If tester collides on that tile...
                    #mainwriter.write(f"positive tile at {x*64}, {y*64}")
                    tester.move_ip(64, 0) #tester moves horizontally to the next tile.
                    if x==15: #If this is the final tile of the row, which does collide with tester...
                        return 8-y #It calls the winning row out.
                else:
                    tester.move_ip(-64*x,0) #If the tester does not collide, it moves back to x=1.
                    #mainwriter.write(f"row {8-y} is not full. Tester moved to {tester.x}, {tester.y}\n ")
                    break #and then it breaks out of this row's loop.
            #This is only accessed if the represented row is incomplete, a complete row returns out of the function.
            tester.move_ip(0, 64) #This assumes the tester was successfully placed at x=1. and moves "down" one tile since the top left corner is 1,1 and down means a higher Y value.
        return -1 #Return -1 to signify no filled lines.


    def remove(self):
        """
        makes a tetronimo inactive and uncollidable. Inactive tetronimos should be removed from the list of tetronimos present in-game and will eventually be deleted by
        python's automated memory cleanup.
        """
        self.active=False
        self.coordinates=[[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
        self.collision_boxes=[]