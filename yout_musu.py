import pygame, sys, random, os
from pygame.locals import *

#define colors
class Colors:
    green = (1, 68, 33)
    black = (0, 0, 0)
    teal = (0, 128, 128)
    white = (255, 255, 255)
    red = (255, 0, 0)
    gray = (128, 128, 128)

#define buttons
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.15), int(height*0.15)))
        self.scale = scale
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos() # get mouse position
        if self.rect.collidepoint(pos): # check if mouse over and clicked conditions
            # self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1.1), int(self.image.get_height()*1.1)))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        Background().blit(self.image, (self.rect.x, self.rect.y))
        return action
    
class Text:
    def text():
        font1 = pygame.font.SysFont('comicsansms', 30)
        font2 = pygame.font.SysFont('comicsansms', 20)
        # font3 = pygame.font.SysFont('comicsansms', 20)
        text1 = font1.render('Esi sveicināts lielajā meža spēlē!', False, Colors.white) # text, antialiasing, color
        text2 = font2.render('Spied z, v, t vai g, lai mainītu spēles fonu!', False, Colors.white)
        # text3 = font3.render('Spied d, lai iepazītu citus meža dzīvniekus!', False, white) # text, antialiasing, color
        text1 = Background.screen.blit(text1, (10, 10))
        text2 = Background.screen.blit(text2, (10, 50))
        # text3 = Background.screen.blit(text3, (10, 80))
        return text1, text2 #, text3

#background
class Background:
    def __init__(self):
        screen_width = 1000
        screen_height = 600
        screen = pygame.display.set_mode((screen_width,screen_height))
        self.background = screen.fill(Colors.green)
        self.game_name = pygame.display.set_caption('Lielā dabas spēle "Mežs"')
        game_icon = pygame.image.load('citi_atteli/skuja.png')
        game_icon = pygame.display.set_icon(game_icon)       
        
        winter_image = pygame.image.load("ziemas_bg.jpg")
        winter_image = pygame.transform.scale(winter_image, (1000, 600))
        summer_image = pygame.image.load("vasaras_bg.jpg")
        summer_image = pygame.transform.scale(summer_image, (1000, 600))

        memory_game_image = pygame.image.load("forest_buttons/memory_eng.png").convert_alpha()
        learn_forest_image = pygame.image.load("forest_buttons/learnforest_eng.png").convert_alpha()  
        self.memory_game_button = Button(10, 100, memory_game_image, 1).draw()
        self.learn_forest_button = Button(10, 200, learn_forest_image, 1).draw()     
      

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
#     def __init__(self):
#         self.state = Background()
        
#     def intro(self):
#         pass
        # Background()
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         pygame.quit() 
        #     if event.type == MOUSEBUTTONDOWN:
        #         self.state = 'main_game'
        #     # if event.type == pygame.KEYDOWN:
        #     #     button_press_time = pygame.time.get_ticks()
        #     #     Background.screen.fill((255,255,255))
                
        # # current_time = pygame.time.get_ticks()
        # # if current_time - button_press_time > 2000:
        # #     Background.screen.fill((0,0,0))
        # # print(f"current_time {current_time} button_press time: {button_press_time}")
        

        # #Background.background.blit(background,(0,0))

        # # crosshair_group.draw(Background.screen)
        # # crosshair_group.update()
        # pygame.display.flip()       
        
    # def main_game(self):
    #     pass
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit() 
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         crosshair.shoot()
            # if event.type == pygame.KEYDOWN:
            #     button_press_time = pygame.time.get_ticks()
        #     #     Background.screen.fill((255,255,255))
                
        # # current_time = pygame.time.get_ticks()
        # # if current_time - button_press_time > 2000:
        # #     Background.screen.fill((0,0,0))
        # # print(f"current_time {current_time} button_press time: {button_press_time}")
        
        # pygame.mouse.set_visible(False)

        # # current_time = 0
        # # button_press_time = 0 #var rēķināt laiku, līdz beidz spēli

        # crosshair = Crosshair()
        # crosshair_group = pygame.sprite.Group()
        # crosshair_group.add(crosshair)

        # #Target
        # target_group = pygame.sprite.Group()
        # for target in range(20):
        #     new_target = Target(random.randrange(0,screen_width), random.randrange(0,screen_height))
        #     target_group.add(new_target)
        
        # Background.screen.blit(background,(0,0))
        # target_group.draw(Background.screen)
        # crosshair_group.draw(Background.screen)
        # crosshair_group.update()
        # pygame.display.flip()
        
    # def Scene_manager(self):
    #     Background()
    #     if self.state == 'intro':
    #         self.intro()
    #     if self.state == 'main_game':
    #         self.main_game()
    pass
       
#general setup
pygame.init()
clock = pygame.time.Clock()
# scene = Scene()
# background = Background()

# Background().run()
# while True:
#     # Scene().Scene_manager()
#     clock.tick(60)

Background()   
while True:
    # running = True 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            # running = False
        if Background().memory_game_button:
            print('memory_game')
        if Background().learn_forest_button:
            print('learn forest')
        elif event.type == KEYDOWN:
            if event.key == K_g:
                background = Background.screen.fill(Colors.green)         
            elif event.key == K_t:
                background = Background.screen.fill(Colors.teal)   
            elif event.key == K_z:
                background = Background.screen.blit(Background.winter_image, (0, 0))
            elif event.key == K_v:
                background = Background.screen.blit(Background.summer_image, (0, 0)) 
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()