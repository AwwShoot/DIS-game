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

top_boundary=pygame.rect.Rect(0,-1, 1024,1)
bottom_boundary=pygame.rect.Rect(0,512,1024,1)
left_boundary=pygame.rect.Rect(0,0,1,512)
right_boundary=pygame.rect.Rect(1024,0,1,512)
boundaries=(top_boundary, bottom_boundary, left_boundary, right_boundary)

#Initializing the pong ball and snake objects
pong_ball=Ball([512,50], [4,8])
player_one =Snake([[0,0], [0,1], [0,2], [0,3]])
player_two=Snake([[15,0], [15,1], [15,2], [15,3]])
mainwriter.write("initialized")




#running the game loop


clock = pygame.time.Clock()
while True :
    moved=False
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainwriter.end()
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if player_one.last_move!="right":
                    player_one.move("left")
                    moved = True
            elif event.key == pygame.K_d:
                if player_one.last_move != "left":
                    player_one.move("right")
                    moved = True
            elif event.key == pygame.K_w:
                if player_one.last_move != "down":
                    player_one.move("up")
                    moved = True
            elif event.key == pygame.K_s:
                if player_one.last_move != "up":
                    player_one.move("down")
                    moved = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if player_two.last_move != "right":
                        player_two.move("left")
                        moved = True
                elif event.key == pygame.K_RIGHT:
                    if player_two.last_move != "left":
                        player_two.move("right")
                        moved = True
                elif event.key == pygame.K_UP:
                    if player_two.last_move != "down":
                        player_two.move("up")
                        moved = True
                elif event.key == pygame.K_DOWN:
                    if player_two.last_move != "up":
                        player_two.move("down")
                        moved = True



    if not moved :
        player_one.move(player_one.last_move)
    player_one.check_collision(player_two.collision_boxes, boundaries, 1)
    pong_ball.move()
    pong_ball.check_collision(player_one.collision_boxes, player_two.collision_boxes, boundaries)
    screen.blit(ball, (pong_ball.coordinates[0], pong_ball.coordinates[1]))
    for box in player_one.collision_boxes:
        screen.blit(p1, box)
    for box in player_two.collision_boxes:
        screen.blit(p2, box)

    if not moved :
        player_two.move(player_two.last_move)
    player_two.check_collision(player_one.collision_boxes, boundaries, 2)
    pong_ball.move()
    pong_ball.check_collision(player_two.collision_boxes, player_two.collision_boxes, boundaries)




    pygame.display.update()

    clock.tick(2.75)

# theres some jank with snake movement, ill see if i can fix it, but if not i vote we
# call it a feature and say that the snake likes to drift

    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/
