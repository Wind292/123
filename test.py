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


def handle_collisions():
    global player_can_jump, isgrounded

    for tile in GroundTileList + GrassTileList:
        if player_tophitbox.colliderect(tile):
            player.y = tile.y + tile.height
            player_yVel = 0
            player_airtime = 0
            player_can_jump = True
            isgrounded = True
            break
        elif player_bottomhitbox.colliderect(tile):
            player.y = tile.y - player.height
            player_yVel = 0
            player_airtime = 0
            isgrounded = True
            break
    else:
        isgrounded = False




firstframeonground = False
player_bottomhitbox = pygame.Rect(player.x+1, player.y+99,98,2)
player_tophitbox = pygame.Rect(player.x+1, player.y-1,98,2)
tophitboxcollided = False
# Main loop
while True:
    player_airtime += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    print(isgrounded)
    if isgrounded:
        player_yVel = 0
        player_airtime = 0
        player_can_jump = True
    else:
        player.y += player_yVel

    player_yVel = (player_gravity * player_airtime) + player_yVel

    handle_collisions()

    if key[pygame.K_LEFT]:
        player.x -= player_speed
        handle_collisions()
    if key[pygame.K_RIGHT]:
        player.x += player_speed
        handle_collisions()

    if key[pygame.K_UP] and player_can_jump:
        player_can_jump = False
        player_yVel = player_jump_speed
        player_airtime = 0
        handle_collisions()
        player.y -=1
    
    
    
    if key[pygame.K_a]:
        for tile in GroundTileList + GrassTileList:
            tile.x += 20
        player.x += 20
    if key[pygame.K_d]:
        for tile in GroundTileList + GrassTileList:
            tile.x -= 20
        player.x -= 20
    if key[pygame.K_w]:
        for tile in GroundTileList + GrassTileList:
            tile.y += 20
        player.y += 20
    if key[pygame.K_s]:
        for tile in GroundTileList + GrassTileList:
            tile.y -= 20       
        player.y -= 20

        
    screen.fill('gray')
    for tile in GroundTileList:
        screen.blit(ground, (tile.x, tile.y))

    for tile in GrassTileList:
        screen.blit(grass, (tile.x, tile.y))


    player_bottomhitbox = pygame.Rect(player.x + 1, player.y + 99, 98, 2)
    player_tophitbox = pygame.Rect(player.x + 1, player.y - 1, 98, 2)

    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 0, 255), player_tophitbox)

 
    

    
    firstframeonground =False
    
    tophitboxcollided = False
    pygame.display.update()
    clock.tick(fps)
