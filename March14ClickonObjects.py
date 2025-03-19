import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("fish mouse imput")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
chest = 1
chest2  = 1
ticker = 0

#load in the image and make transparent
chestImg1 = pygame.image.load("chest1.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg1, [255,0,255])
#load in the image and make transparent
chestImg2 = pygame.image.load("chest2.jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg2, [255,0,255])

chestImg1_0 = pygame.image.load("TreasureChest-1.png (1).jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg1, [255,0,255])

chestImg2_0 = pygame.image.load("TreasureChest-2.png (1).jpg").convert_alpha()
pygame.Surface.set_colorkey (chestImg2, [255,0,255])

class Chest:
    def __init__(self):
        self.Frame_num = 0
        self.X_Pos = random.randint(0, 800-self.Chest_Width)
        self.Y_Pos = random.randit(0, 600-self.Chest_Height)
        Game_Screen.blit(self.Chest_Image, (self.X_Pos, self.Y_Pos), (0, self.Chest_Height*self.Frame_num, self.Chest_Width, self.Chest_Height))
        


while 1: #game loop###########################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        print(mousePos) #this is to help you know where to set these boundaries
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #check if you've clicked on the chest
            if mousePos[0]>238 and mousePos[0] < 355 and mousePos[1]>130 and mousePos[1]<230:
                chest = 2

            if mousePos[0]>558 and mousePos[0] < 690 and mousePos[1]>130 and mousePos[1]<235:
                chest2 = 2
         
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos        
    
    #update/physics section----------------------

    #keep chest open for 50 game loops:
    if chest == 2:
        ticker+=1
        if ticker >= 200:
            ticker = 0
            chest = 1

    if chest2 == 2:
        ticker+=1
        if ticker >= 200:
            ticker = 0
            chest2 = 1

    #render section------------------------------
    
    screen.fill((0,0,180))# Clear the screen
    
    #draw background image
    if chest == 1:
        screen.blit(chestImg1, (240, 140))
    elif chest == 2: 
        screen.blit(chestImg2, (240, 140))

    if chest2 == 1:
        screen.blit(chestImg1_0, (560, 140))
    elif chest2 == 2: 
        screen.blit(chestImg2_0, (560, 140))
    
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()