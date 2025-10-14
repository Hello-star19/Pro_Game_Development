import pygame
import random
import time

from pygame.locals import* 


pygame.init()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(1000,700))
bg = pygame.display.set_mode((1000,700))
# gaming variables
score = 0
start_time = time.time()
font_style = pygame.font.SysFont("Arial",20)





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



# class for recyclable items
class non_recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
nrgroup = pygame.sprite.Group()
for i in range(30):
    item = non_recycle() 
    item.rect.x = random.randint(20,940)
    item.rect.y = random.randint(20,640)
    nrgroup.add(item)


class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
bingroup = pygame.sprite.Group()
for i in range(1):
    bins = bin() 
    bins.rect.x = (10)
    bins.rect.y = (10)
    bingroup.add(bins)





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # total time
    total_time = time.time()- start_time
    if total_time > 20:
        message = font_style.render("Game over",True,"Blue")
    else: 
        bg.blit(background,(0,0))
        timer = font_style.render(str(20-int(total_time)), True,"White")
        bg.blit(timer,(100,0))
        rgroup.draw(bg)
        nrgroup.draw(bg)
        bingroup.draw(bg)
        # Controlling the bin
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bins.rect.y-= 1
        if keys[pygame.K_DOWN]:
            bins.rect.y+= 1
        if keys[pygame.K_RIGHT]:
            bins.rect.x+= 1
        if keys[pygame.K_LEFT]:
            bins.rect.x-= 1

   

    pygame.display.update()
pygame.quit()





