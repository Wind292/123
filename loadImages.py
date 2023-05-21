import pygame

def load():
    grass = pygame.image.load("assets/images/grass.png")
    ground = pygame.image.load("assets/images/ground.png")
    
    grass = pygame.transform.scale(grass, (100,100)).convert()
    ground = pygame.transform.scale(ground, (100,100)).convert()
    return grass,ground