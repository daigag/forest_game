import pygame, sys, random, os
from pygame.locals import *

#general setup
pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('ziemas_bg.jpg')
background = pygame.transform.scale(background, (screen_width,screen_height))

class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('forest_buttons/pointer_2.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.klick = pygame.mixer.Sound('sounds/win.wav')
    def catch(self):
        self.klick.play()
        pygame.sprite.spritecollide(Pointer(), Hide_and_seek.object_group(), True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
class Object(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.image = random.choice(os.listdir('meza_dzivnieki')) 
        self.image = pygame.image.load(os.path.join('meza_dzivnieki', self.image)) 
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        
class Hide_and_seek():
    def __init__(self):
        pygame.init()
        clock.tick(60)
        pygame.mouse.set_visible(False)
        self.running = True
    
    def object_group():
        object_group = pygame.sprite.Group()
        for object in range(20):
            new_target = Object(random.randrange(0,screen_width), random.randrange(0,screen_height))
            object_group.add(new_target)
        return object_group
    
    def run(self):
        pointer = Pointer()
        pointer_group = pygame.sprite.Group()
        pointer_group.add(pointer)
        
        # screen.blit(background,(0,0))                  
        Hide_and_seek.object_group().draw(background)   
        # pointer_group.draw(screen) 
        # pointer_group.update()
        pygame.display.flip()   
    
        while self.running:
            
            # pointer_group.draw(screen) 
            # pointer_group.update()
            # #screen.blit(background, (0,0))
            # #Hide_and_seek.object_group().draw(screen)   
            # #pygame.display.update()             
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pointer.catch()
                    
                                    
            screen.blit(background,(0,0))                  
            #Hide_and_seek.object_group().draw(screen)   
            pointer_group.draw(screen)
            pointer_group.update()
            pygame.display.update()   
  
if __name__ == '__main__':        
    Hide_and_seek().run()