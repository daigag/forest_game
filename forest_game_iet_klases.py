import pygame
from pygame.locals import *
import random
import os

green = (20, 90, 15)
black = (0, 0, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128)

winter_image = pygame.image.load("ziemas_bg.jpg")
winter_image = pygame.transform.scale(winter_image, (1000, 600))
summer_image = pygame.image.load("vasaras_bg.jpg")
summer_image = pygame.transform.scale(summer_image, (1000, 600)) 

screen = pygame.display.set_mode((1000, 600))
background = screen.fill(green)
game_name = pygame.display.set_caption('Lielā dabas spēle "Mežs"')
game_icon = pygame.image.load('citi_atteli/skuja.png')
game_icon = pygame.display.set_icon(game_icon)

width = screen.get_width()
height = screen.get_height()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.2), int(height*0.2)))
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
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
class Forest_game:
    def __init__(self):
        pygame.init()
        self.running = True

    def text():
        font1 = pygame.font.SysFont('comicsansms', 30)
        font2 = pygame.font.SysFont('comicsansms', 20)
        font3 = pygame.font.SysFont('comicsansms', 20)
        text1 = font1.render('Esi sveicināts lielajā meža spēlē!', False, white) # text, antialiasing, color
        text2 = font2.render('Spied z, v, t vai g, lai mainītu spēles fonu!', False, white)
        text3 = font3.render('Spied d, lai iepazītu citus meža dzīvniekus!', False, white) # text, antialiasing, color
        text1 = screen.blit(text1, (10, 10))
        text2 = screen.blit(text2, (10, 50))
        text3 = screen.blit(text3, (10, 80))
        return text1, text2, text3
        
    def forest_animal_image():
        animal = random.choice(os.listdir('meza_dzivnieki')) # choose random image from folder
        animal_image = pygame.image.load(os.path.join('meza_dzivnieki', animal)).convert() # if convert - with white background, if without - without background
        animal_image = pygame.transform.scale(animal_image, (300, 300)) # resize image
        animal_image = screen.blit(animal_image, (350,150)) # draw image on screen
        animal_file_name = os.path.splitext(str(animal))[0] # get file name without extension
        f_font = pygame.font.SysFont('comicsansms', 30)
        f_text = f_font.render(animal_file_name, True, white) # text, antialiasing, color
        f_text = screen.blit(f_text, (450, 450))    
        return animal_image, f_text
      
    def other_forest_things():
        other = random.choice(os.listdir('citi_atteli')) # choose random image from folder
        other_image = pygame.image.load(os.path.join('citi_atteli', other)).convert() # load image
        other_image = pygame.transform.scale(other_image, (300, 350)) # resize image
        other_image = screen.blit(other_image, (350,100)) # draw image on screen
        return other_image
    
    def image_file_name():
        image_file_name.font = pygame.font.SysFont('comicsansms', 20)
        image_file_name = image_file_name.font.render(os.path.splitext(str(Forest_game.other_forest_things()))[0], True, black) # text, antialiasing, color
        image_file_name = screen.blit(image_file_name, (350, 200))
        return image_file_name
            
    def run(self):   
        while self.running:
            self.intro = Forest_game.text()
            memory_game_image = pygame.image.load("meza_dzivnieki/vilks.png").convert_alpha()
            learn_forest_image = pygame.image.load("meza_dzivnieki/lapsa.png").convert_alpha()
            self.memory_game_button = Button(300, 300, memory_game_image, 1).draw()
            self.learn_forest_button = Button(600, 300, learn_forest_image, 1).draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if self.memory_game_button:
                    print('memory_game')
                if self.learn_forest_button:
                    print('learn forest')
                elif event.type == KEYDOWN:
                    if event.key == K_g:
                        self.background = screen.fill(green)         
                    elif event.key == K_t:
                        self.background = screen.fill(teal)   
                    elif event.key == K_z:
                        self.background = screen.blit(winter_image, (0, 0))
                    elif event.key == K_v:
                        self.background = screen.blit(summer_image, (0, 0)) 
                    elif event.key == K_d:
                        self.animal = Forest_game.forest_animal_image()
                    elif event.key == K_o:
                        self.other = Forest_game.other_forest_things()
                pygame.display.flip()
        pygame.quit()
    
if __name__ == '__main__':
    Forest_game().run()
    
    
