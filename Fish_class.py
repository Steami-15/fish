# 
# pygame.Surface.set_colorkey (self.fishImage, [255,0,255]) What does this do?
# 
# 
import pygame
import random
import time

pygame.init()
Game_Screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fish_Tank")


class Fish:
    def __init__(self):
        self.Fish_Width = 0
        self.Fish_Height= 0
        self.Fish_Image = fish_image
        self.X_Pos = random.randint(0, 800-self.Fish_Width)
        self.Y_Pos = random.randint(0,600-self.Fish_Height)
        self.is_alive = True
        self,speed = 1
        self.direction = 1
        self.xDir = random.randint(-1,1)
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time()

    def move(self):
        # Move the fish
        self.X_Pos += self.xDir* self.speed
        self.Y_Pos += self.yDir * self.speed

        # Change direction every 3 seconds
        if time.time() - self.last_change_time > 3:  
            self.xDir = random.randint(-1,1)
            self.yDir = random.randint(-1,1)
            self.last_change_time = time.time() #reset the time

        # Check for collision with walls and change direction
        if self.X_Pos <= 0 or self.X_Pos >= 800-self.Fish_Width:
            self.xDir *= -1
        if self.Y_Pos <= 0 or self.Y_Pos>= 600-self.Fish_Height:
            self.yDir *= -1
    def draw(self, screen):
        screen.blit(self.fishImage, (self.X_Pos, self.Y_Pos))
