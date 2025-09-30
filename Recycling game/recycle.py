import pygame
import random
import time

from pygame.locals import* 

pygame.init()

bg = pygame.display.set_mode((1000,700))

# class for recyclable items
class recycle(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
robjects = ["box.png", "paper.png","wood.png"]
rgroup = pygame.sprite.Group()
for i in range(40):
    item = recycle(random.choice(robjects)) 
    item.rect.x = random.randint(20,940)
    item.rect.y = random.randint(20,640)
    rgroup.add(item)






run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    rgroup.draw(bg)
    pygame.display.update()
pygame.quit()


