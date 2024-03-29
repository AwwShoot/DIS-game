#middle click a method or variable to see it's declaration.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from snake import Snake

from logwriter import mainwriter
from tetronimo import Tetronimo
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
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

mainwriter.write("initializing\n")

screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Ultimate Sneetrong")



p1 = pygame.image.load(mainwriter.resource_path('src/assets/bluesquare.png'))
p2 = pygame.image.load(mainwriter.resource_path('src/assets/redsquare.png'))
ball = pygame.image.load(mainwriter.resource_path('src/assets/ball.png'))
bg = pygame.image.load(mainwriter.resource_path('src/assets/background.png'))
lbs = pygame.image.load(mainwriter.resource_path('src/assets/lightbluesquare.png'))
lrs = pygame.image.load(mainwriter.resource_path('src/assets/lightredsquare.png'))
awiy = pygame.image.load(mainwriter.resource_path('src/assets/winscreenred.png'))
awib = pygame.image.load(mainwriter.resource_path('src/assets/winscreenblue.png'))
title = pygame.image.load(mainwriter.resource_path('src/assets/titlescreen.png'))
frame1 = pygame.image.load(mainwriter.resource_path('src/assets/frame1.png'))
frame2 = pygame.image.load(mainwriter.resource_path('src/assets/frame2.png'))
frame3 = pygame.image.load(mainwriter.resource_path('src/assets/frame3.png'))
frame4 = pygame.image.load(mainwriter.resource_path('src/assets/frame4.png'))
frame5 = pygame.image.load(mainwriter.resource_path('src/assets/frame5.png'))
frame6 = pygame.image.load(mainwriter.resource_path('src/assets/frame6.png'))

placeholder = pygame.image.load(mainwriter.resource_path('src/assets/placeholder.png'))
andyou = pygame.image.load(mainwriter.resource_path('src/assets/credits.png'))
htp = pygame.image.load(mainwriter.resource_path('src/assets/HowTo.png'))


vs = pygame.mixer.Sound(mainwriter.resource_path('src/assets/victoryscreech.wav'))










top_boundary=pygame.rect.Rect(0,-1, 1024,1)
bottom_boundary=pygame.rect.Rect(0,512,1024,1)
left_boundary=pygame.rect.Rect(-1,0,1,512)
right_boundary=pygame.rect.Rect(1024,0,1,512)
boundaries=(top_boundary, bottom_boundary, left_boundary, right_boundary)
tetronimos=[]



#Initializing the pong ball and snake objects
pong_ball=Ball([512,50], [6,3])
player_one =Snake([[0,0], [0,1], [0,2], [0,3]], 1)
player_two=Snake([[15,0], [15,1], [15,2], [15,3]], 2)

# initializing misc variables
respawn_time=15
p1_respawn=0
p2_respawn=0
Victory=False
credits=False
howto=False
gamestart = False
mainwriter.write("initialized \n")


def creditscreen():
    pogchamp = True
    while pogchamp:
        screen.blit(andyou, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pogchamp = False

def howtogame():
    gamer = True
    while gamer:
        screen.blit(htp, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gamer = False

#running the game loop

while gamestart == False :
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.fill(black)
    screen.blit(title, (0, 0))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if 858 + 122 > mouse[0] > 858 and 38 + 28 > mouse[1] > 38:
            if click[0] == 1:
                gamestart=True
        if 858 + 122 > mouse[0] > 858 and 111 + 28 > mouse[1] > 111:
            if click[0] == 1:
                creditscreen()
                gamestart = False
        if 858 + 122 > mouse[0] > 858 and 184 + 29 > mouse[1] > 184:
            if click[0] == 1:
                howtogame()
                gamestart = False
    else:
        pass
    pygame.display.update()


#right and proper coordinates for startgame : (858, 38, 122, 28)
#right and proper coordinates for credits : (858, 111, 122, 28)
#right and proper coordinates for howto : (858, 184, 122, 29)

count=0
clock = pygame.time.Clock()
while Victory==False :
    player_one.moving=False
    player_two.moving=False

    for event in pygame.event.get():
        #Quit clause
        if event.type == pygame.QUIT:
            mainwriter.end()
            pygame.quit()
            quit()
        # Movement
        if event.type == pygame.KEYDOWN and player_one.removed==False:
            if event.key == pygame.K_a:
                if player_one.last_move!="right":
                    player_one.move("left")

            elif event.key == pygame.K_d:
                if player_one.last_move != "left":
                    player_one.move("right")

            elif event.key == pygame.K_w:
                if player_one.last_move != "down":
                    player_one.move("up")

            elif event.key == pygame.K_s:
                if player_one.last_move != "up":
                    player_one.move("down")


        #Player 2 input
        if event.type == pygame.KEYDOWN and player_two.removed==False:
            if event.key == pygame.K_LEFT:
                if player_two.last_move != "right":
                    player_two.move("left")

            elif event.key == pygame.K_RIGHT:
                if player_two.last_move != "left":
                    player_two.move("right")

            elif event.key == pygame.K_UP:
                if player_two.last_move != "down":
                    player_two.move("up")

            elif event.key == pygame.K_DOWN:
                if player_two.last_move != "up":
                    player_two.move("down")




#right and proper coordinates: (858, 38, 122, 28)


    if not player_one.moving and count==1 and not player_one.last_move=="":
        player_one.move(player_one.last_move)

    if not player_two.moving and count==1 and not player_two.last_move=="":
        player_two.move(player_two.last_move)


    #screen.blit(frame1, (512, 64))
    #screen.blit(frame2, (512, 64))
    #screen.blit(frame3, (512, 64))
    #screen.blit(frame4, (512, 64))
    #screen.blit(frame5, (512, 64))
    #screen.blit(frame6, (512, 64))


    frame=pong_ball.move()



    # Tetronimo movement

    for piece in tetronimos:
        if not piece.active:
            tetronimos.pop(tetronimos.index(piece))
        if piece.splitting:
            tetronimos.extend(piece.build_from_list())
            piece.remove()
            tetronimos.pop(tetronimos.index(piece))
            continue
        piece.move(boundaries, tetronimos)

    #respawn countdown
    if p1_respawn>0:
        if p1_respawn==1:
            player_one.replace()
        p1_respawn-=1

    if p2_respawn>0:
        if p2_respawn==1:
            player_two.replace()
        p2_respawn-=1

    # Display update
    screen.blit(bg, (0, 0))#See how things are here? What if we were to simply copy it again and shift the numbers to reflect destruction?
    if pong_ball.respawn_timer==0:
        screen.blit(ball, (pong_ball.coordinates[0], pong_ball.coordinates[1]))
    if frame == 1:
        screen.blit(frame1, pong_ball.coordinates)
    if frame == 2:
        screen.blit(frame2, pong_ball.coordinates)
    if frame == 3:
        screen.blit(frame3, pong_ball.coordinates)
    if frame == 4:
        screen.blit(frame4, pong_ball.coordinates)
    if frame == 5:
        screen.blit(frame5, pong_ball.coordinates)
    if frame == 6:
        screen.blit(frame6, pong_ball.coordinates)





    #we can still communicate here
    #why are we deleting things? I am cutting/pasting them to just be in order. ok, jsut asking
        #There will be no functional change because only one of these statements should activate per frame anyways
        # This code sharing thing HATES indentation

    if frame == 7:
        screen.blit(frame6, pong_ball.coordinates)
    if frame == 8:
        screen.blit(frame5, pong_ball.coordinates)
    if frame == 9:
        screen.blit(frame4, pong_ball.coordinates)
    if frame == 10:
        screen.blit(frame3, pong_ball.coordinates)
    if frame == 11:
        screen.blit(frame2, pong_ball.coordinates) #Everywhere involved that *could* be where it hangs. Like in this if statement.
        print("Is it working here?")
    if frame == 12:
        screen.blit(frame1, pong_ball.coordinates)

#now do i run it?
#I am a little stumped. Time for the most powerful debugging tool: Throwing print() statements everywhere to see exactly what happens. ok, where do we throw them first?

    for box in player_one.collision_boxes:
        screen.blit(p1, box)
    for box in player_two.collision_boxes:
        screen.blit(p2, box)
     # SET UP TETRONIMO SPRITES HERE
    for piece in tetronimos:
        if piece.player==1:
            for box in piece.collision_boxes:
                screen.blit(lbs, box)
        else:
            for box in piece.collision_boxes:
                screen.blit(lrs, box)
    pygame.display.update()

    # scoring check.
    if pong_ball.colliding==True:
        scorer = pong_ball.score(left_boundary, right_boundary)
        if scorer == 1 and player_one.removed == False:
            tetronimos.append(player_one.tetrify())
            p1_respawn = respawn_time / 3
        elif scorer == 2 and player_two.removed == False:
            tetronimos.append(player_two.tetrify())
            p2_respawn = respawn_time / 3

    # Collision check
    tetronimo_boxes=[]
    for piece in tetronimos:
        for box in piece.collision_boxes:
            tetronimo_boxes.append(box)

    pong_ball.check_collision(player_one, player_two, boundaries, tetronimo_boxes)
    if player_one.removed==False:
        p1_collided=player_one.check_collision(player_two.collision_boxes, boundaries, tetronimos)
    if player_two.removed==False:
        p2_collided=player_two.check_collision(player_one.collision_boxes, boundaries, tetronimos)
    if p1_collided:
        p1_respawn=respawn_time
        p1_collided=False
    if p2_collided:
        p2_respawn=respawn_time
        p2_collided=False



    #victory check
    if len(tetronimos)!=0:
        winning_line=Tetronimo.check_lines(tetronimo_boxes)
        if winning_line!=-1:
            #USE VICTORY SCREENS HERE
            Victory=True

#uh it worked sometimes, it is now sometimes not noticing collison w/ the wall and then not scoring a point The wall as in the edge of the screen wall or all collisions? edge of the screen, it sometimes just yeets past it and doesnt score
    #Does the ball respawn from going out of bounds?
    #eventually, ill share screen again just be muted


    count+=1
    if count>1:
        count=0
    clock.tick(8)

#End of game, main game loop is finished

mainwriter.write(f"line {winning_line} cleared")
if tetronimos[len(tetronimos)-1].player==1:
    screen.blit(awib, (0, 0))
    pygame.display.update()
else:
    screen.blit(awiy, (0, 0))
    pygame.display.update()
while True:



    for event in pygame.event.get():
        #Quit clause
        if event.type == pygame.QUIT:
            mainwriter.end()
            pygame.quit()
            quit()

    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See Python help at https://docs.python.org/3/tutorial/
# See PyGame help at https://www.pygame.org/docs/

'''

while Victory:
    pygame.mixer.Sound.play(vs)
    pygame.mixer.music.stop()
'''