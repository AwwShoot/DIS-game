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

screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Ultimate Sneetrong")

p1 = pygame.image.load(r'src\assets\bluesquare.png')
p2 = pygame.image.load(r'src\assets\redsquare.png')
ball = pygame.image.load(r'src\assets\ball.png')

top_boundary=pygame.rect.Rect(0,0, 1024,1)
bottom_boundary=pygame.rect.Rect(0,512,1024,1)
left_boundary=pygame.rect.Rect(0,0,1,512)
right_boundary=pygame.rect.Rect(1024,0,1,512)
boundaries=(top_boundary, bottom_boundary, left_boundary, right_boundary)

#Initializing the pong ball and snake objects
pong_ball=Ball([512,50], [1,2])
player_one =Snake([[-1,-1], [-1,-1], [-1,-1], [-1,-1]])
player_two=Snake([[-1,-1], [-1,-1], [-1,-1], [-1,-1]])
mainwriter.write("initialized")






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



    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
