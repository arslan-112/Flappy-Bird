import pygame
import random
import math
import time
from pygame import mixer

 
pygame.init()

#creates screen
screen = pygame.display.set_mode((912,768))

#Background
Background = pygame.image.load(r'D:\Python Programs\Flappy Bird\background.webp')

title = pygame.display.set_caption('Flappy Bird')

player_img = pygame.image.load(r'D:\Python Programs\Flappy Bird\flappybirbicon.png')

#Bg sound
mixer.music.load(r'D:\Python Programs\Flappy Bird\Stay.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)


clock = pygame.time.Clock()


class Bird():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        
        self.vel = 10
    def player(self):
        screen.blit(player_img,(self.x,self.y))
        

#Pipes

pipeup1 = [pygame.image.load(r'D:\Python Programs\Flappy Bird\pipedown4.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipedown2.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipedown3.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipedown1.png')]
pipeupX = []
pipeupY = [0,0,0,0]
pipeupX_change = 5


pipedown1 = [pygame.image.load(r'D:\Python Programs\Flappy Bird\pipeup3.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipeup1.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipeup2.png'),
    pygame.image.load(r'D:\Python Programs\Flappy Bird\pipeup4.png')]

#pipespacing
space = 62
pipedownX = []
pipedownY = [362,446,406,490]
pipedownX_change = 5

num_pipes = 4
x_pos = 512
for i in range(num_pipes):
    
    pipeupX.append(x_pos)
    
    pipedownX.append(x_pos)


    x_pos += 230

bird = Bird(300,350)

#Score
score_val = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_val), True, (255,255,255))
    screen.blit(score,(x,y))



#Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)
#Game Won Text
won_font = pygame.font.Font("freesansbold.ttf", 64)

#Character sizes
width_of_bird = 40
height_of_bird = 28
#pipe initial positions
pipe1x = 512
pipe2x = 512 + 230
pipe3x = 512 + 230*2
pipe4x = 512 + (230*2) + 230



def collision_with_top_pillar(i,length_of_p):
    if bird.y <= (length_of_p - space+47) and bird.y <= length_of_p and (bird.x+width_of_bird) >= p1_newx and bird.x <= (60+ p1_newx):
        return True

                        
    return False

def collision_with_bottom_pillar(i,length_of_p):
    

    if (bird.y ) >= (length_of_p+5) and (bird.x+width_of_bird) >= p1_newxd and bird.x <= (60+p1_newxd):
        return True
    return False

#Lenghts of pipes

len_of_pipeup1 = 260
len_of_pipedown1 = 362

len_of_pipeup2 = 342
len_of_pipedown2 = 446

len_of_pipeup3 = 300
len_of_pipedown3 = 406

len_of_pipeup4 = 382
len_of_pipedown4 = 490

def game_over_font():
    over = over_font.render("YOU LOST!", True, (255,255,255))
    screen.blit(over,(210,250))

def game_won():
    win_score = won_font.render("YOU WON!", True, (255,255,255))
    screen.blit(win_score,(210,250))

def pipeup(x,y,i):
    screen.blit(pipeup1[i],(x,y))

def pipedown(x,y,i):
    screen.blit(pipedown1[i],(x,y))

def pipemovement(i):
    pipeupX[i] -= pipeupX_change
    pipedownX[i] -= pipedownX_change 
    a = pipeupX[i]
    b = pipedownX[i]
    return a,b             
game = True
valid = True
while game:
    clock.tick(25)
    screen.fill((0,0,0))  #for background color
    screen.blit(Background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bird.y > 0:
        
        bird.y -= bird.vel
        
    else:
        bird.y += bird.vel +3





    #Pipe movement
    for i in range(num_pipes):

        

        if pipeupX[i] <= 0 or pipedownX[i] <=0:
            pipeupX[i] = 912
                  
            pipedownX[i] = 912
            
            if valid:
                score_val += 1
        if game:
            p1_newx,p1_newxd = pipemovement(i)   
            
            
        
        if score_val == 35:
            
            for i in range(num_pipes):
                pipeupY[i] = -800
                pipedownY[i] = -800
                bird.vel = 0
                
                game_won()
                
                game = False
        
        if i == 0:
            collide_up = collision_with_top_pillar(i,len_of_pipeup1)
            collide_down = collision_with_bottom_pillar(i,len_of_pipedown1)
        elif i ==1:
            collide_up = collision_with_top_pillar(i,len_of_pipeup2)
            collide_down = collision_with_bottom_pillar(i,len_of_pipedown2)
        elif i == 2:
            collide_up = collision_with_top_pillar(i,len_of_pipeup3)
            collide_down = collision_with_bottom_pillar(i,len_of_pipedown3)
        elif i == 3:
            collide_up = collision_with_top_pillar(i,len_of_pipeup4)
            collide_down = collision_with_bottom_pillar(i,len_of_pipedown4)



        
        # collide_down = collision_with_bottom_pillar(len_of_pipedown,i)
        
        if collide_up or collide_down or bird.y >768:
            

             
            
                         
            
            
            pipedownY[i] = -500
            pipedownX[i] = -500
            game_over_font()
            


            
            valid = False
            game = False
        




            
            

        pipeup(pipeupX[i],pipeupY[i],i)
        pipedown(pipedownX[i],pipedownY[i],i)



    show_score(textX,textY)
    bird.player()
    pygame.display.update()
pygame.quit()
    



