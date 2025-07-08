import pygame
from pygame.locals import 
import time

pygame.init()

background = pygame.display.set_mode((500, 500))
# loading the images 
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,(500,500))
spaceship = pygame.image.load ("spaceship.png")
spaceship = pygame.transform.scale(spaceship, (150, 150))
style = pygame.font.SysFont("Calibri", 40)


# initial position of the player

xpos = 190
ypos = 110

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                ypos = ypos - 12
            if event.key == K_DOWN:
                ypos = ypos + 10
            if event.key == K_LEFT:
                xpos = xpos - 5
            if event.key == K_RIGHT:
                xpos = xpos + 5

    background.blit(bg ,(0,0) )
    background.blit(spaceship,(xpos, ypos))
    ypos = ypos + 10
    time.sleep(0.2)
    if ypos > 500:
        background.blit(bg, (0,0))
        text = style.render("Game Over!", True, "white")
        background.blit(text,(200,250))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()

    elif ypos <= 0:
        background.blit(bg, (0,0))
        text = style.render("You Win!", True, "green")
        background.blit(text,(200,250))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()

    pygame.display.update()





    








