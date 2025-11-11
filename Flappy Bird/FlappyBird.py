import pygame
from pygame.locals import *

import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
width = 864
height = 768

bg = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

font = pygame.font.SysFont("Arial",20)
colour = (100,19,45)

# Gaming variables 

ground_scroll = 0 
scroll_speed = 5
bird_flight = False
end_title = False
pipe_gap = 160
pipe_frequency = 2000
score = 0
pipe_pass = False

# Loading images 
background = pygame.image.load("bg.png")
ground_image = pygame.image.load("ground.png")
restart = pygame.image.load("restart.png")
# class for the bird 
class bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0 
        for i in range(1,4):
            img = pygame.image.load(f"bird{i}.png")
            self.images.append(img)

        self.rect = self.image.get_rect()

run = True

while run == True:
    bg.blit(background, (0,0))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()













