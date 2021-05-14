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
        boolean splitting flags a tetronimo as ready for the splitting/rebuilding algorithms.
        """
        self.ID=Tetronimo.next_ID
        Tetronimo.next_ID+=1
        self.active=True
        self.player=player
        self.splitting=False

        self.coordinates=coordinates
        self.collision_boxes=[]
        for pair in coordinates:
            # boxes are an extra pixel tall downwards. This is so they can check collision immediately below them without moving or other funky stuff.
            self.collision_boxes.append(rect.Rect(pair[0]*64, pair[1]*64, 64, 64))

    def move(self, boundaries, tetronimos):
        """

        :param boundaries: list of collision boxes for boundaries
        :param tetronimos: list of tetronimos present in the world.
        checks if a tetronimo can move first before dropping it down.
        """
        testing_boxes=[]

        for box in self.collision_boxes:
            testing_boxes.append(rect.Rect(box.x, box.y+64, 1, 1))

        for tester in testing_boxes:
            if tester.collidelist(boundaries) != -1:
                return

        for piece in tetronimos:
            if piece.ID!=self.ID:
                for tester in testing_boxes:
                    if tester.collidelist(piece.collision_boxes) != -1:
                        return

        for box in self.collision_boxes:
            box.move_ip(0, 64)
        for pair in self.coordinates:
            pair[1]+=1

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


    def check_adjacent(self, center, boxes, index, value):
        """

        :param center: The center piece being checked
        :param boxes: The list of peices being checked
        :param index: The index of the pair to compare
        :param value: The value to compare the center and pair by
        :return: The INDEX of the adjacent pair in the coords array.
        """
        if index==1:
            opposite_index=0
        else:
            opposite_index=1

        piece_list=[]
        for box in boxes:
            piece_list.append([box.x, box.y])

        center_coords=[center[0], center[1]]
        for pair in piece_list:
            if center_coords[index]+value*64==pair[index] and center_coords[opposite_index]==pair[opposite_index]:
                print(f"code says that {center[0]/64}, {center[1]/64} is adjacent to {pair[0]/64}, {pair[1]/64}")
                return piece_list.index(pair)
        return None

    def build_from_list(self):
        """
        Builds new tetronimo pieces out of a list of coordinates.
        Assumes the coordinate pairs are those of a tetronimo that was just partially destroyed.
        :return: a list of pieces made from the original list of coordinates.
        """

        original_length=len(self.collision_boxes)
        if original_length!=len(self.coordinates):
            self.coordinates=self.make_coordinates(self.collision_boxes)
        print(f"{original_length} is the start") #debug info

        unbuilt_pieces=[]
        final_pieces=[] #instantiation

        while len(self.collision_boxes)>0: #as long as the tetronimo has pieces.


            origin = self.collision_boxes.pop(0) #The first tile in the list will be the origin for the new piece.

            self.coordinates.pop(0)
            new_piece=[]
            new_piece.append(origin) #instantiation.

            for center in new_piece:
                index = self.check_adjacent(center, self.collision_boxes, 0, -1)
                if index is not None and index < len(self.collision_boxes):
                    new_piece.append(self.collision_boxes.pop(index))
                    print("Found an adjacent tile (left). Adding it to the new piece and removing it from the original list")

                index = self.check_adjacent(center, self.collision_boxes, 0, 1)
                if index is not None and index < len(self.collision_boxes):
                    new_piece.append(self.collision_boxes.pop(index))
                    print("Found an adjacent tile (right). Adding it to the new piece and removing it from the original list")

                index = self.check_adjacent(center, self.collision_boxes, 1, -1)
                if index is not None and index < len(self.collision_boxes):
                    new_piece.append(self.collision_boxes.pop(index))
                    print("Found an adjacent tile (up). Adding it to the new piece and removing it from the original list")

                index = self.check_adjacent(center, self.collision_boxes, 1, 1)
                if index is not None and index < len(self.collision_boxes):
                    new_piece.append(self.collision_boxes.pop(index))
                    print("Found an adjacent tile (down). Adding it to the new piece and removing it from the original list")

            unbuilt_pieces.append(new_piece)
            print(f"New piece has been added with a length of {len(new_piece)}. The original list should be that many items shorter")

        for set in unbuilt_pieces:
            coordinates=[]
            for box in set:
                coordinates.append([box.x/64, box.y/64])

            final_pieces.append(Tetronimo(coordinates, self.player))


        self.splitting=False
        print(f"there should be {len(final_pieces)} chunks")
        if final_pieces!= []:
            return final_pieces
        else:
            return [self]

    def split(self, coords):
        valid = False
        position=-1
        for box in self.collision_boxes:
            position+=1
            if box.x == coords[0]*64 and box.y == coords[1]*64:
                self.collision_boxes.pop(position)
                valid = True
                print(f"valid coordinates {coords[0]} {coords[1]}")
                break
        if valid:
            self.splitting=True
        else:
            print(f"invalid coordinates {coords[0]} {coords[1]}")
            for pair in self.coordinates:
                mainwriter.print_coordinates(pair)

    def make_coordinates(self, collision_boxes):
        new_coords=[]
        for box in collision_boxes:
            new_coords.append([box.x/64, box.y/64])

        return new_coords
