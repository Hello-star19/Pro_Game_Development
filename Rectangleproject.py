import pygame
pygame.init()

bg = pygame.display.set_mode((400,500))

c1 = (0,7,19)
c2 = (0, 100, 230)
c3 = (20, 197, 145)
c4 = (251, 100, 50)
# Adding background colour
bg.fill(c3)
pygame.display.update()
Run = True

#creating a class for the rectangle
class rectangle():
    def __init__(self, color, size):






while Run:
    for event in pygame.event.get():   # Fetches all events happening
        if event.type == pygame.QUIT:
            Run = False

pygame.quit()
        