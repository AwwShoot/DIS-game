#middle click a method or variable to see it's declaration.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from snake import Snake
import logwriter
from logwriter import log
from ball import Ball

"""
click the green play button in the top right to run the code. 
It will only run this specific file.
All other code must be referenced and ran here.
placing words between three sets of "" quotation marks makes a multi-line comment. this writing is not read or used in the program, but allows notes to be placed
using a # hashtag can make single line comments for smaller stuff.
"""
#Initializing the game
log.write("Start of a new Ultimate Sneetrong debug log\n")
screen = pygame.display.set_mode((960, 560))
pygame.display.set_caption("Ultimate Sneetrong")
#Creating test display shapes
starting_box = pygame.rect.Rect(0, 0, 500, 500)

blue_color=pygame.color.Color(0,0,255,70)

pygame.draw.rect(screen, blue_color, starting_box)
screen.set_at((50,50),blue_color)
#An area of the screen must be updated with this command for any visual changes to take place
pygame.display.update(starting_box)
log.write("done loading\n")
#Initializing the pong ball and snake objects
pong_ball=Ball([2.0,2.0], [0.0,0.0])
player_one =Snake([[0,0], [0,1], [1,1], [1,0]])
#Testing the logwriter as well as the two gameplay objects
logwriter.write_coordinates(player_one.get_position())
logwriter.write_position(pong_ball.get_position())
player_one.move("up")
player_one.move("right")
player_one.move("right")
player_one.move("down")
player_one.move("left")
player_one.move("up")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
