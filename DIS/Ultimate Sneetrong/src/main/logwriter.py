log=open("src/logs/game_log", 'w')
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

def write_coordinates(coordinates):
    """

    :param coordinates: A list of coordinate pairs
    :return: returns nothing but writes the coordinate pairs into the log
    """
    log.write(" printing coordinates:")
    for i in coordinates:
        x=i[0]
        y=i[1]
        log.write(f"({x}, {y})")
    log.write("\n")


def write_position(coordinates):
    """

    :param coordinates: A single coordinate pair as a list object of two ints or floats
    :return: returns nothing, but writes the coordinate pair into the log
    """
    log.write(" printing position:")
    log.write(f"({coordinates[0]}, {coordinates[1]}) \n")