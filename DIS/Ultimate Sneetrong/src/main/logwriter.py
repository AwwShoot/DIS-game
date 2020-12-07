
"""
The first line of this file immediately creates a new log file when this is imported (I.E. when main is started)
log is now the namespace to refer to this file. The file is write-only, but if necessary I can make it readable as well
log.write(<string object or literal>) will print that string object or literal into the file
a string literal is anything between two "" quotation marks.
a string object is any namespace that refers to a string literal
name="Billy": name is an object for the literal 'Billy'
a string literal with a lowercase f directly in front of it is a formatted string literal.
This means any name placed within {} curly brackets will be printed as it's actual value, such as how write_coordinates() prints the values of the coordinates
the \ backslash can be used for fancy formatting as well. 
\n creates a new line \', \", and \\ are examples of the backslash being used to "break out" a character, making it no longer serve it's normal function but be printed instead.

"""
import sys
import os
class Logwriter:
    last_string=""
    last_strings=["", "", ""]
    repeat_count=0

    def __init__(self, directory):
        pass


    def write_coordinates(self, coordinates):
        pass
        """

        :param coordinates: A list of coordinate pairs
        :return: returns nothing but writes the coordinate pairs into the log
        """
        '''
        output =" printing coordinates:"
        for i in coordinates:
            x=i[0]
            y=i[1]
            output+= f"({x}, {y})"
        output+= "\n"
        self.write(output)'''


    def write_position(self, coordinates):
        pass
        """
        :param coordinates: A single coordinate pair as a list object of two ints or floats
        :return: returns nothing, but writes the coordinate pair into the log
        """
        '''
        output =" printing position:" + f"({coordinates[0]}, {coordinates[1]}) \n"
        self.write(output)'''

    """
    Not technically necessary, but use this instead of log.write in instances where you anticipate the same line repeating over and over and over to save space.
    """

    def write(self, string):
        pass
        '''
            self.log.write(string)'''





    def end(self):
        pass
        '''
        self.log.write(f"the following strings were repeated a total of {self.repeat_count} times \n")
        for i in self.last_strings:
            self.log.write(i)
            self.log.write("\n")'''
    #Yoinked potential fix for pyinstaller from stackoverflow. I put it here since every file imports logwriter
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS <-- the temp file made when the .exe is ran
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)





mainwriter=Logwriter("src/logs/game_log")