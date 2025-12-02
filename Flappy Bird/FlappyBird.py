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
last_pipe = pygame.time.get_ticks()-pipe_frequency
score = 0
pipe_pass = False
game_over = False

# Loading images 
background = pygame.image.load("bg.png")
ground_image = pygame.image.load("ground.png")
restart = pygame.image.load("restart.png")
# class for the bird 
class bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0 
        for i in range(1,4):
            img = pygame.image.load(f"bird{i}.png")
            self.images.append(img)

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.yspeed = 0
        self.clicked = False
    #update function
    def update(self):
        global bird_flight, game_over
        #gravity 
        if bird_flight == True:
            self.yspeed += 0.5
            if self.yspeed > 7:
                self.yspeed = 7
            if self.rect.bottom <= 768:
                self.rect.y += int(self.yspeed)
        if not game_over:
            if pygame.mouse.get_pressed()[0]==1 and not self.clicked:
                self.clicked = True
                self.yspeed = -6
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked = False

            bird_flap = 5
            self.counter +=1
            if self.counter > bird_flap:
                self.counter = 0
                self.index +=1 
                if self.index >= len(self.images):
                    self.index = 0 
                self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.yspeed*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index,-90])
# class for the pipe
class pipe(pygame.sprite.Sprite):
    def __init__(self, x,y, pos):
        super().__init__()
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipe_gap/2)]
        elif pos == -1:
            self.rect.topleft = [x,y+int(pipe_gap/2)]
    def update(self):
        self.rect.x-= scroll_speed
        if self.rect.right<0:
            self.kill
# class for restart button 
class restart():
    def __init__(self, x,y):
        self.image= pygame.image.load("restart.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        mousepos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousepos)

run = True
# Group for the sprites
birds = pygame.sprite.Group()
bird_object = bird(200,390)
birds.add(bird_object)

pipes = pygame.sprite.Group()


while run == True:
    clock.tick(fps)
    bg.blit(background, (0,0))
    pipes.draw(bg)
    bg.blit(ground_image, (ground_scroll,650))
    birds.draw(bg)  
    birds.update() 

    ground_scroll -= scroll_speed
    if abs(ground_scroll) >30 :
        ground_scroll = 0
    # pipe generation
    if bird_flight == True and game_over == False:
        # time in seconds game started
        game_time = pygame.time.get_ticks()
        if game_time - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            pipe_bottom = pipe(864,384 + pipe_height,-1 )
            pipe_top = pipe(864,384 + pipe_height,1 )
            pipes.add(pipe_bottom)
            pipes.add(pipe_top)
            last_pipe = game_time
        pipes.update()
        ground_scroll -= scroll_speed
        if abs(ground_scroll) >30 :
            ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not bird_flight and not game_over:
            bird_flight = True

    pygame.display.update()
pygame.quit()













