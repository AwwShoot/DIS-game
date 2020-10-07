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
black = (0, 0, 0)

log.write("Start of a new Ultimate Sneetrong debug log\n")
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Ultimate Sneetrong")
#flashing the images on screen

p1 = pygame.image.load(r'C:\Users\Stephen Gray\PycharmProjects\DIS-game\DIS\Ultimate Sneetrong\src\assets\bluesquare.png')
p2 = pygame.image.load(r'C:\Users\Stephen Gray\PycharmProjects\DIS-game\DIS\Ultimate Sneetrong\src\assets\redsquare.png')
ball = pygame.image.load(r'C:\Users\Stephen Gray\PycharmProjects\DIS-game\DIS\Ultimate Sneetrong\src\assets\ball.png')


#need something better than the absolute path here

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while True :
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1_change = -64
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = 64
                y1_change = 0
            elif event.key == pygame.K_w:
                y1_change = -64
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = 64
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    screen.blit(p1, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(5)


    

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
pong_ball.move()
pong_ball.set_velocity([1.0,1.0])
pong_ball.move()
pong_ball.move()


while True:
    pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
