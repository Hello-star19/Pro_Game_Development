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
class rectangles():
    def __init__(self, color, size):
        self.surface = bg
        self.color = color
        self.size = size
    # Draw function
    def draw(self):
        self.rectangle = pygame.draw.rect(self.surface, self.color, self.size)

rectangle1 = rectangles(c2, (10, 10, 50, 60))
rectangle2 = rectangles(c4, (80, 90, 100, 140))
rectangle3 = rectangles(c1, (340,390, 50, 100))






while Run:
    for event in pygame.event.get():   # Fetches all events happening
        if event.type == pygame.QUIT:
            Run = False
    rectangle1.draw()
    rectangle2.draw()
    rectangle3.draw()
    pygame.display.update()


pygame.quit()
        