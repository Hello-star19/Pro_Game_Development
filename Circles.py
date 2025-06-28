import pygame
pygame.init()

background = pygame.display.set_mode((400,500))

c1 = (243, 196, 72)
c2 = (255, 255, 255)
c3 = (213, 131, 236)
c4 = (255, 0 , 255)

background.fill(c4)
pygame.display.update()

# class for the circle
class circles():
    def __init__(self, color, position, size, width = 0):
        self.surface = background
        self.color = color
        self.position = position
        self.size = size 
        self.width = width

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.position, self.size, self.width)

#object creation

circle1 = circles(c1, (250, 250), 120)
circle2 = circles(c3, (250, 250), 90, 7)



run = True
while run:
    for events in pygame.event.get():
        if events.type  == pygame.QUIT: 
            run = False
    circle1.draw()
    circle2.draw()
    pygame.display.update()

pygame.quit()


 

