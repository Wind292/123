import pygame
import sys
import os
import pymunk.pygame_util
from pytmx.util_pygame import load_pygame
import loadImages as img


pymunk.pygame_util.positive_y_is_up = False

pygame.init()
screen = pygame.display.set_mode((2000, 1080))

tmx_data = load_pygame("assets/maps/baseparkor.tmx")

# Loads images
grass, ground = img.load()


# Get tile layers and put them in lists with pygame rects
layer = tmx_data.get_layer_by_name("Ground")
GroundTileList = []
for x, y, surf in layer:
    # checks if tile is air
    if not surf == 0:
        rect = pygame.Rect(x * 100, y * 100, 100, 100)
        GroundTileList.append(rect)

del rect, layer

layer = tmx_data.get_layer_by_name("Grass")
GrassTileList = []
for x, y, surf in layer:
    # checks if tile is air
    if not surf == 0:
        rect = pygame.Rect(x * 100, y * 100, 100, 100)
        GrassTileList.append(rect)

del rect, layer

TileList = GroundTileList + GrassTileList

clock = pygame.time.Clock()
fps = 60

gravity = .1


player = pygame.Rect(100,100,100,100)

player_speed = 15
player_jump_speed = -500
player_can_jump = False
player_airtime = 0
player_gravity = gravity
player_yVel = 0
player_maxvel = 10
freecam = False
isgrounded = False

firstframeonground = False
player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
player_tophitbox = pygame.Rect(player.x+1, player.y-1,98,2)
tophitboxcollided = False
# Main loop
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
    #prevents sticking underground
    for tile in TileList:
        if player_bottomhitbox.colliderect(tile) and player.colliderect(tile):
            player.y = tile.y - player.height
            
    for tile in TileList:
        if player_tophitbox.colliderect(tile) and player.colliderect(tile):
            player_yVel = 0
            player.y = tile.y + 101                
    

    
    for tile in TileList:
        if player_bottomhitbox.colliderect(tile):
            isgrounded = True
            break
        else:
            isgrounded = False

        
    
    # Player movement
    key = pygame.key.get_pressed()
    
    if isgrounded:
        player_yVel = 0
        player_airtime = 0
        player_can_jump = True 
    else:
        player.y += player_yVel    
    
    

    player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
    for tile in TileList:
        
        while player.colliderect(tile) and tophitboxcollided == False and player_bottomhitbox.colliderect(tile):
            
            player.y -= 1
            player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
                    
        
    
    


    player_yVel = (player_gravity * player_airtime) + player_yVel

    for tile in TileList:
        if player_tophitbox.colliderect(tile):
            tophitboxcollided = True
            break
        
    for tile in TileList:
        if player_tophitbox.colliderect(tile) and player.colliderect(tile):
            player_yVel = 0
            player.y = tile.y + 101
            
    #checks for underground and pushes up



    
    
    #terminal veloc
    if player_airtime < player_maxvel:
        player_airtime += 1
        


        
    #left and right
    topcoll = False
    for tile in TileList:
        if player_tophitbox.colliderect(tile):
            topcoll = True
    
    
    if key[pygame.K_LEFT]:
        player.x -= player_speed
        for tile in TileList:
            while player.colliderect(tile) and topcoll == False:
                player.x += 1
                
    if key[pygame.K_RIGHT]:
        player.x += player_speed
        for tile in TileList:
            while player.colliderect(tile) and topcoll == False:
                player.x -= 1
    
            

        
        
    if key[pygame.K_UP] and player_can_jump:
         #jumps
            player_can_jump = False 
            player_yVel = -20
            player_airtime = 0   
            player.y -= 1 
    
    
    
    if key[pygame.K_a]:
        for tile in TileList:
            tile.x += 20
        player.x += 20
    if key[pygame.K_d]:
        for tile in TileList:
            tile.x -= 20
        player.x -= 20
    if key[pygame.K_w]:
        for tile in TileList:
            tile.y += 20
        player.y += 20
    if key[pygame.K_s]:
        for tile in TileList:
            tile.y -= 20       
        player.y -= 20

        
    screen.fill('gray')
    for tile in GroundTileList:
        screen.blit(ground, (tile.x, tile.y))

    for tile in GrassTileList:
        screen.blit(grass, (tile.x, tile.y))


    player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
    player_tophitbox = pygame.Rect(player.x+1, player.y-1,98,2)


    pygame.draw.rect(screen, (255, 0, 0), player)
    # pygame.draw.rect(screen, (0, 0, 255), player_bottomhitbox)
    pygame.draw.rect(screen, (0, 0, 255), player_tophitbox)

 
    

    
    firstframeonground =False
    
    tophitboxcollided = False
    pygame.display.update()
    clock.tick(fps)

import pygame
import sys
import os
from pytmx.util_pygame import load_pygame
import loadImages as img


pygame.init()
screen = pygame.display.set_mode((2000, 1080))

tmx_data = load_pygame("assets/maps/huge.tmx")

# Loads images
grass, ground = img.load()


# Get tile layers and put them in lists with pygame rects
layer = tmx_data.get_layer_by_name("Ground")
GroundTileList = []
for x, y, surf in layer:
    # checks if tile is air
    if not surf == 0:
        rect = pygame.Rect(x * 100, y * 100, 100, 100)
        GroundTileList.append(rect)

del rect, layer

layer = tmx_data.get_layer_by_name("Grass")
GrassTileList = []
for x, y, surf in layer:
    # checks if tile is air
    if not surf == 0:
        rect = pygame.Rect(x * 100, y * 100, 100, 100)
        GrassTileList.append(rect)

del rect, layer

TileList = GroundTileList + GrassTileList

clock = pygame.time.Clock()
fps = 60

gravity = .1

checkinscreen = pygame.Rect(0,0,2000, 1080)

player = pygame.Rect(250,100,100,100)
player_speed = 15

player_can_jump = False
player_airtime = 0
player_gravity = gravity
player_yVel = 0
player_maxvel = 10
freecam = False
isgrounded = False

firstframeonground = False
player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
player_tophitbox = pygame.Rect(player.x+1, player.y-1,98,2)
tophitboxcollided = False
# Main loop
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
    #prevents sticking underground
    for tile in TileList:
        if player_bottomhitbox.colliderect(tile) and player.colliderect(tile):
            player.y = tile.y - player.height
            
    for tile in TileList:
        if player_tophitbox.colliderect(tile) and player.colliderect(tile):
            player_yVel = 0
            player.y = tile.y + 101                
    

    
    for tile in TileList:
        if player_bottomhitbox.colliderect(tile):
            isgrounded = True
            break
        else:
            isgrounded = False

        
    
    # Player movement
    key = pygame.key.get_pressed()
    
    if isgrounded:
        player_yVel = 0
        player_airtime = 0
        player_can_jump = True 
    else:
        player.y += player_yVel    
    
    

    player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
    for tile in TileList:
        
        while player.colliderect(tile) and tophitboxcollided == False and player_bottomhitbox.colliderect(tile):
            
            player.y -= 1
            player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
                    
        
    
    


    player_yVel = (player_gravity * player_airtime) + player_yVel

    for tile in TileList:
        if player_tophitbox.colliderect(tile):
            tophitboxcollided = True
            break
        
    for tile in TileList:
        if player_tophitbox.colliderect(tile) and player.colliderect(tile):
            player_yVel = 0
            player.y = tile.y + 101
            
    #checks for underground and pushes up



    
    
    #terminal veloc
    if player_airtime < player_maxvel:
        player_airtime += 1
        


        
    #left and right
    topcoll = False
    for tile in TileList:
        if player_tophitbox.colliderect(tile):
            topcoll = True
    
    
    if key[pygame.K_LEFT]:
        player.x -= player_speed
        for tile in TileList:
            while player.colliderect(tile) and topcoll == False:
                player.x += 1
  
    if key[pygame.K_RIGHT]:
        player.x += player_speed
        for tile in TileList:
            while player.colliderect(tile) and topcoll == False:
                player.x -= 1

    
            

        
        
    if key[pygame.K_UP] and player_can_jump:
         #jumps
            player_can_jump = False 
            player_yVel = -20
            player_airtime = 0   
            player.y -= 1 
    
    
    
    if key[pygame.K_a]:
        for tile in TileList:
            tile.x += 20
        player.x += 20
    if key[pygame.K_d]:
        for tile in TileList:
            tile.x -= 20
        player.x -= 20
    if key[pygame.K_w]:
        for tile in TileList:
            tile.y += 20
        player.y += 20
    if key[pygame.K_s]:
        for tile in TileList:
            tile.y -= 20       
        player.y -= 20

        
    screen.fill('gray')
    for tile in GroundTileList:
        if tile.colliderect(checkinscreen):
            screen.blit(ground, (tile.x, tile.y))

    for tile in GrassTileList:
        if tile.colliderect(checkinscreen):
            screen.blit(grass, (tile.x, tile.y))


    player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
    player_tophitbox = pygame.Rect(player.x+1, player.y-1,98,2)


    pygame.draw.rect(screen, (255, 0, 0), player)
    # pygame.draw.rect(screen, (0, 0, 255), player_bottomhitbox)
    # pygame.draw.rect(screen, (0, 0, 255), player_tophitbox)

 
    

    
    firstframeonground =False
    
    tophitboxcollided = False
    pygame.display.update()
    clock.tick(fps)