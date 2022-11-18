import pygame, sys, random, os
from pygame.locals import *

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('forest_buttons/pointer_2.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('sounds/win.wav')
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.image = random.choice(os.listdir('meza_dzivnieki')) 
        self.image = pygame.image.load(os.path.join('meza_dzivnieki', self.image)) 
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        
class Scene():
    def __init__(self):
        self.running = True
   
        
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
            # if event.type == pygame.KEYDOWN:
            #     button_press_time = pygame.time.get_ticks()
            #     screen.fill((255,255,255))
                
        # current_time = pygame.time.get_ticks()
        # if current_time - button_press_time > 2000:
        #     screen.fill((0,0,0))
        # print(f"current_time {current_time} button_press time: {button_press_time}")
        

        screen.blit(background,(0,0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()
        
      
#general setup
pygame.init()
clock = pygame.time.Clock()
scene = Scene()


screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('ziemas_bg.jpg')
background = pygame.transform.scale(background, (screen_width,screen_height))
pygame.mouse.set_visible(False)

# current_time = 0
# button_press_time = 0 #var rēķināt laiku, līdz beidz spēli

crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target(random.randrange(0,screen_width), random.randrange(0,screen_height))
    target_group.add(new_target)

while True:
    scene.run()
    clock.tick(60)