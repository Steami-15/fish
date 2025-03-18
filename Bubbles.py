class Bubbles:
    def __init__(self, y):
        self.y = y
        self.x = random.randint(50, 700)
        self.top_bubbles = pygame.transform.flip(bubbles_image, False, True)

        
    def move(self):
        self.y -= 4 #Move pipes to the left
        #print("moving bubbles")
        self.x += random.randint(-2, 2)
    def draw(self):        
        screen.blit(self.top_bubbles, (self.x, self.y))
