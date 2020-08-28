# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame

"""
click the green play button in the top right to run the code. 
It will only run this specific file.
All other code must be referenced and ran here.
"""
log=open("src/logs/game_log", 'w')
log.write("Start of a new Ultimate Sneetrong debug log\n")
screen = pygame.display.set_mode((960, 560))
pygame.display.set_caption("Ultimate Sneetrong")
starting_box = pygame.rect.Rect(0, 0, 500, 500)
starting_box.normalize()
blue_color=pygame.color.Color(0,0,255,70)
blue_color.normalize()
pygame.draw.rect(screen, blue_color, starting_box)
screen.set_at((50,50),blue_color)
pygame.display.update(starting_box)
log.write("done loading")
"""
the loop keeps the script loaded so the screen is onscreen. 
press CTRL+C or click the red square in pyCharm to force close the code.
"""
log.write("hello")

while True:
    log.write("cheese ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
