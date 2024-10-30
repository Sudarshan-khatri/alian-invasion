# import the module pygame for create the game
import pygame

# import the module random to generate the random value of enenmy
import random

# initialize the system for game
pygame.init()

#create teh window of game 
screen=pygame.display.set_mode((800,650))

# set the game name 
pygame.display.set_caption("Alian Invasion")
# set the image on window 

w_img=pygame.image.load('alian.png')
pygame.display.set_icon(w_img)

# set the background image 
bg_img=pygame.image.load('back.jpg')
bg_img=pygame.transform.scale(bg_img, (800,650))

# initialize the background color
bg_color=(230,167,255)

#set the  rocket in window
player_img=pygame.image.load('rocket.png')
playerX=365
playerY=575
player_change=0

# set the enemy in the window 
enemy_img=pygame.image.load('enemy.png')
enemyX=random.randint(0,800)
enemyY=random.randint(0,650)
enemyX_change=0.3
enemyY_change=20
# rocket function 
def f_player(x,y):
    screen.blit(player_img,(x,y))

# enemy function 
def e_enemy(x,y):
    screen.blit(enemy_img,(x,y))
# use while loop for run the game untill quit the game 
running=True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    # set the keystroke to control the rocket with the help of keyboard button
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_change-=0.6
            if event.key==pygame.K_RIGHT:
                player_change+=0.6
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_change=0
    # display the background image
    screen.blit(bg_img,(0,0))
  
    # set the boundaries for the rocket
    playerX+=player_change
    if playerX>=736:
        playerX=736
    elif playerX<=0:
        playerX=0  
    
    # set the boundaries for the enemy
    enemyX+=enemyX_change
    if enemyX>=776:
        enemyX_change=-0.6
        enemyY+=enemyY_change
    elif enemyX<=0:
        enemyX_change=0.6
        enemyY+=enemyY_change

    # call the function
    f_player(playerX,playerY)
    e_enemy(enemyX,enemyY)
   
    #update the display
    pygame.display.flip()
pygame.display.update()

