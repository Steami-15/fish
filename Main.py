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
Mouse_X_Pos = 0
Mouse_Y_Pos = 0
Mouse_Pos = (Mouse_X_Pos, Mouse_Y_Pos)







#######################################
while Playing_Game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
        if event.type == pygame.MOUSEMOTION:
            Mouse_Pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(Mouse_Pos) #### This should be changed to something else later...
        
    Tick_Speed.tick(60)
    Time += 1
    Game_Screen.blit(Background, (0, 0))
    pygame.display.flip()
pygame.quit
