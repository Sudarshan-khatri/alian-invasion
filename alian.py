# import the module pygame for create the game
import pygame
# initialize the system for game
pygame.init()
#create teh window of game 
screen=pygame.display.set_mode((800,650))
# set the game name 
pygame.display.set_caption("Alian Invasion")
# set the image on window 
w_img=pygame.image.load('alian.png')
pygame.display.set_icon(w_img)
# initialize the background color
bg_color=(230,167,255)
#set the first player in window
player_img=pygame.image.load('rocket.png')
playerX=365
playerY=575

# player function 
def f_player():
    screen.blit(player_img,(playerX,playerY))
# use while loop for run the game untill quit the game 
running=True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #set the background color
    screen.fill(bg_color)
    # call the function
    f_player()
   
    #update the display
    pygame.display.flip()
pygame.display.update()

