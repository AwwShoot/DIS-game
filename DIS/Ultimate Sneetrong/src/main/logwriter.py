log=open("src/logs/game_log", 'w')

"""
Breaks a list of coordinate pairs into a string.
"""
def writecoords(coordinates):
    log.write(" printing coordinates:")
    for i in coordinates:
        x=i[0]
        y=i[1]
        log.write(f"({x}, {y})")
    log.write("\n")