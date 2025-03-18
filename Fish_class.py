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
    def __init__(self, Width, Height, Fish_Image):
        self.Fish_Width = Width
        self.Fish_Height = Height
        self.Fish_Image = Fish_Image
        super().__init__()
