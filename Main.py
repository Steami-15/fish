#This is going to be the place where all our code goes when finished ############# Go to me for putting it in before in
import pygame
import random
import time

pygame.init()
Game_Screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fish_Tank")
Background = pygame.image.load('Fish Tank background.png').convert_alpha()
Playing_Game = True
Tick_Speed = pygame.time.Clock()
Time = 0






#######################################
while Playing_Game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
    Tick_Speed.tick(60)
    Time += 1
    Game_Screen.blit(Background, (0, 0))
    pygame.display.flip()
pygame.quit
