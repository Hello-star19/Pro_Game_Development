import pygame
import random
import time

from pygame.locals import* 


pygame.init()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(1000,700))
you_win = pygame.image.load("you_win.jpg")
you_win = pygame.transform.scale(you_win,(1000,700))
you_loose = pygame.image.load("you_loose.jpg")
you_loose = pygame.transform.scale(you_loose,(1000,700))
bg = pygame.display.set_mode((1000,700))
# gaming variables
score = 0
start_time = time.time()
font_style = pygame.font.SysFont("Arial",50)





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



score_text = font_style.render("Your score is:"+str(score),True,"Blue") 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # total time
    total_time = time.time()- start_time
    if total_time > 20:
        if score >= 15:
            bg.blit(you_win,(0,0))
           # message = font_style.render("Game over",True,"Blue")
        else:
            bg.blit(you_loose,(0,0))
    else: 
        bg.blit(background,(0,0))
        timer = font_style.render(str(20-int(total_time)), True,"Blue")
        bg.blit(timer,(100,0))
        rgroup.draw(bg)
        nrgroup.draw(bg)
        bingroup.draw(bg)
        # Controlling the bin
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bins.rect.y-= 1
            if bins.rect.y <= 0:
                bins.rect.y = 0  
        if keys[pygame.K_DOWN]:
            bins.rect.y+= 1
            if bins.rect.y >= 660:
                bins.rect.y = 660  
        if keys[pygame.K_RIGHT]:
            bins.rect.x+= 1
            if bins.rect.x >=970:
                bins.rect.x = 970  
        if keys[pygame.K_LEFT]:
            bins.rect.x-= 1
            if bins.rect.x <= 0:
                bins.rect.x = 0  
        #checking for collisions
        good_items = pygame.sprite.spritecollide(bins,rgroup, True)
        bad_items = pygame.sprite.spritecollide(bins,nrgroup,True)
        for i in good_items:
            score = score + 1
            score_text = font_style.render("Your score is:"+str(score), True, "Blue")
        for i in bad_items:
            score = score - 1
            score_text = font_style.render("Your score is:"+str(score), True, "Blue")
        bg.blit(score_text, (350,0))
    

        
        
   

    pygame.display.update()
pygame.quit()







