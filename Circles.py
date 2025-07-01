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
    def grow(self,factor):
        self.size = self.size + factor
        pygame.draw.circle(self.surface, self.color, self.position, self.size, self.width)




#object creation

circle1 = circles(c1, (200, 250), 120)
circle2 = circles(c3, (200, 250), 90)
circle3 = circles("white", (200, 250), 70)
circle4 = circles("blue", (200, 250), 50)


run = True
while run:
    for events in pygame.event.get():
        if events.type  == pygame.QUIT: 
            run = False
        elif events.type == pygame.MOUSEBUTTONDOWN:
            circle1.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
            pygame.display.update()
        elif events.type == pygame.MOUSEBUTTONUP:
            circle1.grow(1.5)
            circle2.grow(1.5)
            circle3.grow(1.7)
            circle4.grow(1)
            pygame.display.update()
        elif events.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos()
            scircle = circles ("black", coordinates,2)
            scircle.draw()
            pygame.display.update()






pygame.quit()


 



 

