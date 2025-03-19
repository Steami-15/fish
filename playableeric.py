eric_live = pygame.image.load("eric_live (2).png")

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
    
