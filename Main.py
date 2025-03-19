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
Background = pygame.image.load('Fish Tank background.png').convert_alpha()
Playing_Game = True
Tick_Speed = pygame.time.Clock()
Time = 0


class Fish:
    def __init__(self):
        self.Frame_num = 0
        self.Hunger = 100
        self.X_Pos = random.randint(0, 800-self.Fish_Width)
        self.Y_Pos = random.randint(0,600-self.Fish_Height)
        self.Is_Alive = True
        self.Speed = 1
        self.Direction = 1
        self.X_Dir = random.randint(-1,1)
        self.Y_Dir = random.randint(-1,1)
        self.last_change_time = time.time()
        self.Re_Fish_Image = pygame.transform.flip(self.Fish_Image, True, False)
    def Move(self):
        # Move the fish
        self.X_Pos += self.X_Dir* self.Speed
        self.Y_Pos += self.Y_Dir * self.Speed

        # Change Direction every 3 seconds
        if time.time() - self.last_change_time > 3:  
            self.X_Dir = random.randint(-1,1)
            self.Y_Dir = random.randint(-1,1)
            self.last_change_time = time.time() #reset the time

        # Check for collision with walls and change Direction
        if self.X_Pos <= 0 or self.X_Pos >= 800-self.Fish_Width:
            self.X_Dir *= -1
        if self.Y_Pos <= 0 or self.Y_Pos>= 600-self.Fish_Height:
            self.Y_Dir *= -1
        
        if self.X_Dir == -1:
                self.Direction = -1
        if self.X_Dir == 1:
                self.Direction = 1
    def Draw(self):
        if self.Is_Alive == True:
            if self.Direction == 1:
                Game_Screen.blit(self.Fish_Image, (self.X_Pos, self.Y_Pos), (0, self.Fish_Height*self.Frame_num, self.Fish_Width, self.Fish_Height))
            else:
                Game_Screen.blit(self.Re_Fish_Image, (self.X_Pos, self.Y_Pos), (0, self.Fish_Height*self.Frame_num, self.Fish_Width, self.Fish_Height))
                
class GoldFish(Fish):
    def __init__(self, Width, Height):
        self.Fish_Width = Width
        self.Fish_Height = Height
        self.Fish_Image = pygame.image.load('goldfish.png').convert_alpha()
        super().__init__()

class StarFish(Fish):
    def __init__(self, Width, Height):
        self.Fish_Width = Width
        self.Fish_Height = Height
        self.Fish_Image = pygame.image.load('starfish.png').convert_alpha()
        super().__init__()

class Seal(Fish):
    def __init__(self, Width, Height):
        self.Fish_Width = Width
        self.Fish_Height = Height
        self.Fish_Image = pygame.image.load('seal.png').convert_alpha()
        super().__init__()

class Bubbles:
    def __init__(self, y):
        self.y = y
        self.x = random.randint(50, 700)
        self.bubbles = pygame.image.load('bubble.png').convert_alpha()
    def sound(self):
        pygame.mixer.music.load('bubbling2.wav') 
        sound_effect = pygame.mixer.Sound('bubbling2.wav')  
        pygame.mixer.music.play(-1)  # The '-1' argument makes the music loop indefinitely
    def move(self):
        self.y -= 4 #Move pipes to the left
        #print("moving bubbles")
        self.x += random.randint(-2, 2)
    def draw(self):        
        Game_Screen.blit(self.bubbles, (self.x, self.y))

eric_live = pygame.image.load("eric_live (2).png")

player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
ticker = 0
frameWidth = 50
frameHeight = 51
frameNum = 0
offset = 0
def move_player():
    global isOnGround
    global offset
    isOnGround = False
    
    #ground collsion
    if (player[1] >= 450):
        isOnGround = True
        player[3] = 0
        player[1] = 450
    

    #left/right keyboard movement
    if keys[pygame.K_LEFT]:
        if offset > 260 and player[0]>0:
            player[2] = -5
            
            
        elif player[0]>400 and offset < -1500:
            player[2] = -5
            
        elif player[0]>0:
            offset += 5
            
        else:
            player[2]=0
            
    elif keys[pygame.K_RIGHT]:
        if offset > 260 and player[0]>0:
            player[2] = +5
            
        elif player[0]>400 and offset < -1500:
            player[2] = +5
            
        elif player[0]>0:
            offset -= 5
            player[2] = 0
        
        else:
            player [2]=0
    
    #jump mechanics
    if isOnGround == True and keys[pygame.K_UP]:
        player[3] = -15
        isOnGround = False
        
    #apply gravity
    if isOnGround == False:
        player[3] += 1 #gravity
        
    #update player position   
    player[0]+=player[2] #add velocity to position
    player[1]+=player[3]
    Game_Screen.blit(eric_live, (50, player[1]), (frameWidth*frameNum, 0, frameWidth, frameHeight))

class Kelp:
    def __init__(self, X_Pos, Y_Pos):
        self.Kelp_Image = pygame.image.load('Kelp.png').convert_alpha()
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Frame_num = 0
        self.Kelp_Height = 40
        self.Kelp_Width = 40
    def Draw(self, Time):
        Game_Screen.blit(self.Kelp_Image, (self.X_Pos, self.Y_Pos), (0, self.Height*self.Frame_num, self.Width, self.Height))
        if Time % 100 == 0:
            self.Frame_num += 1
            if self.Frame_num > 2:
                self.Frame_num = 0

Fish_School = []
for i in range (5):
    Fish_School.append(GoldFish(24, 24))
    Fish_School.append(StarFish(34, 30))
    Fish_School.append(Seal(112, 56))




while Playing_Game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
    keys = pygame.key.get_pressed()
    Tick_Speed.tick(60)
    Time += 1
    
    for i in range (len(Fish_School)):
        Fish_School[i].Move()

    Game_Screen.blit(Background, (0, 0))
    move_player()
    for i in range (len(Fish_School)):
        Fish_School[i].Draw()

    pygame.display.flip()
pygame.quit
