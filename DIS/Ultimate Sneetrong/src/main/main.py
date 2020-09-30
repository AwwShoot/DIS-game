#middle click a method or variable to see it's declaration.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from snake import Snake

from logwriter import mainwriter

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
mainwriter.write("initializing")
log.write("Start of a new Ultimate Sneetrong debug log\n")
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Ultimate Sneetrong")

p1 = pygame.image.load(r'src\assets\bluesquare.png')
p2 = pygame.image.load(r'src\assets\redsquare.png')
ball = pygame.image.load(r'src\assets\ball.png')

top_boundary=pygame.rect.Rect(0,0, 1024,1)
bottom_boundary=pygame.rect.Rect(0,512,1024,1)
left_boundary=pygame.rect.Rect(0,512,1,512)
right_boundary=pygame.rect.Rect(1024,512,1,512)
boundaries=(top_boundary, bottom_boundary, left_boundary, right_boundary)

#Initializing the pong ball and snake objects
pong_ball=Ball([2.0,2.0], [0.0,0.0])
player_one =Snake([[0,0], [0,1], [1,1], [1,0]])
player_two=Snake([[8,8], [8,7], [8,6], [8,5]])
mainwriter.write("initialized")



#game loop
while True :
    screen.fill(black)
    screen.blit(p1, (960 * .25 - 32, 560 * .5 - 32))
    screen.blit(p2, (960 * .75 - 32, 560 * .5 - 32))
    screen.blit(ball, (pong_ball.coordinates[0], pong_ball.coordinates[1]))
    pong_ball.move()
    pong_ball.check_collision(player_one.collision_boxes, player_two.collision_boxes, boundaries)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()



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





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
