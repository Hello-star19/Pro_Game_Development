import pygame
import time

pygame.init()
bg = pygame.display.set_mode((500,500))
screen1 = pygame.image.load("Christmas1.jpg")
screen1 = pygame.transform.scale(screen1,(500,500))
# loading the fonts
style = pygame.font.SysFont("Times New Roman", 60)

screen2 = pygame.image.load("Christmas2.jpg")
screen2 = pygame.transform.scale(screen2,(500,500))
style2 = pygame.font.SysFont("Ariel", 80)

screen3 = pygame.image.load("Christmas 3.jpg")
screen3 = pygame.transform.scale(screen3,(500,500))
style3 = pygame.font.SysFont("Calibri", 80)



slide = True

while slide:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #slide = False
            pygame.quit()
    bg.blit(screen1,(0,0))
    text1 = style.render("Happy",True,("Blue"))
    text2 = style.render("Christmas", True, ("Green"))
    bg.blit(text1,(170,200))
    bg.blit(text2,(170,240))
    pygame.display.update()
    time.sleep(2)
    bg.blit(screen2, (0,0))
    text3 = style.render("Merry",True,("Red"))
    text4 = style.render("XMas",True, ("Blue"))
    bg.blit(text3,(200, 200))
    bg.blit(text4,(200,250))
    pygame.display.update()
    time.sleep(3)
    bg.blit(screen3,(0,0))
    text5 = style.render("Merry",True,("Blue"))
    text6 = style.render("Christmas", True, ("Green"))
    bg.blit(text5,(170,200))
    bg.blit(text6,(170,240))
    pygame.display.update()
    time.sleep(3)
pygame.quit()

