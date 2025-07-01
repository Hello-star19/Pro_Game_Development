import pygame
from pygame.locals import *
import time

pygame.init()

background = pygame.display.set_mode((500, 500))
# loading the images 
bg = pygame.image.load("bg.jpg")
rocket = pygame.image.load ("rocket.jpg")

# initial position of the player

xpos = 250
ypos = 100

while ypos < 500:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    background.blit(bg ,(0,0) )
    pygame.display.update()
    




