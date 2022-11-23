
import pygame
import random
import os
from pygame.locals import *
from sound import *
from deep_translator import GoogleTranslator

screen = pygame.display.set_mode((1000, 600))


class Learn_forest:
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (1, 68, 33)

    def __init__(self):
        pygame.init()
        self.running = True
        Learn_forest.background()
        pygame.display.update()

    def background():
        pygame.display.set_caption(
            'Learn Forest - learn animals and other forest things')
        icon = pygame.image.load('citi_atteli/an acorn.png')
        icon = pygame.display.set_icon(icon)
        summer_img = pygame.image.load("vasaras_bg.jpg")
        summer_img = pygame.transform.scale(summer_img, (1000, 600))
        screen.blit(summer_img, (0, 0))

    def forest_animal_image(path):
        # choose random image from folder
        animal = random.choice(os.listdir(path))
        # if convert - with white background
        animal_img = pygame.image.load(os.path.join(path, animal)).convert()
        animal_img = pygame.transform.scale(
            animal_img, (300, 300))  # resize image
        # draw image on Learn_forest.
        animal_img = screen.blit(animal_img, (350, 100))
        # get name of image without extension
        animal_name = os.path.splitext(str(animal))[0]
        font = pygame.font.SysFont('comicsansms', 30)  # set font
        text = font.render(
            f'In English: {animal_name}', True, Learn_forest.white)
        text = screen.blit(text, (350, 400))
        latvian = GoogleTranslator(
            source='auto', target='lv').translate(animal_name)
        lithuanian = GoogleTranslator(
            source='auto', target='lt').translate(animal_name)
        latvian = str(latvian)
        lithuanian = str(lithuanian)
        latvian_animal = font.render(
            f'Latviski: {latvian}', True, Learn_forest.white)
        lithuanian_animal = font.render(
            f'Lietuvių: {lithuanian}', True, Learn_forest.white)
        latvian_animal = screen.blit(latvian_animal, (350, 450))
        lithuanian_animal = screen.blit(lithuanian_animal, (350, 500))
        read_english = Read_loud.say(f'This is {animal_name}.')
        return animal_img, latvian_animal, lithuanian_animal, read_english

    def what_is_it():
        font = pygame.font.SysFont('arial black', 50)
        path = os.listdir('meza_dzivnieki')
        guess = random.choice(path)
        guess = os.path.splitext(str(guess))[0]
        text = font.render(f'Is it {guess}?', True, Learn_forest.red)
        text = screen.blit(text, (350, 50))
        read_english = Read_loud.say(f'Is it {guess}?')
        text2 = font.render(f'Your answer (y/n):', True, Learn_forest.red)
        text2 = screen.blit(text2, (100, 450))
        # choose random image from folder
        animal = random.choice(os.listdir('meza_dzivnieki'))
        # if convert - with white background, if without - without background
        animal_img = pygame.image.load(
            os.path.join('meza_dzivnieki', animal)).convert()
        animal_img = pygame.transform.scale(
            animal_img, (300, 300))  # resize image
        # draw image on Learn_forest.
        animal_img = screen.blit(animal_img, (350, 150))
        animal_name = os.path.splitext(str(animal))[0]
        animal_name = print(animal_name)
        str(guess) == str(animal_name)  # compare guess with animal name
        result = print(str(guess) == str(animal_name))
        return text, animal_img, text2, animal_name, guess, result, read_english

    def run(self):
        pygame.init()
        mixer.music.load('sounds/forest_summer.wav')
        mixer.music.play()
        font = pygame.font.SysFont('arial bold', 40)
        ex = font.render(
            'Press "1" to learn animals, press "2" to learn other forest things!', True, Learn_forest.white)
        ex = screen.blit(ex, (70, 70))
        ex2 = font.render(
            'Press "3", if you already know animals and forest things!', True, Learn_forest.white)
        ex2 = screen.blit(ex2, (70, 140))

        base_font = pygame.font.Font(None, 72)
        user_text = ''
        input_rect = pygame.Rect(600, 460, 0, 0)
        color = Learn_forest.green

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        screen.fill((1, 68, 33))
                        return
                    elif event.key == K_1:
                        pygame.key.set_repeat()
                        Learn_forest.background()
                        pygame.display.update()
                        Learn_forest.forest_animal_image('meza_dzivnieki')
                    elif event.key == K_2:
                        pygame.key.set_repeat()
                        Learn_forest.background()
                        pygame.display.update()
                        Learn_forest.forest_animal_image('citi_atteli')
                    elif event.key == K_3:
                        pygame.key.set_repeat()
                        Learn_forest.background()
                        pygame.display.update()
                        Learn_forest.what_is_it()
                        user_text = user_text[:-1]
                    elif event.key == K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    # if Learn_forest.what_is_it() == ('True'):
                        if user_text == "n":
                            text2 = font.render(
                                'Correct! Press "3" for next!', True, Learn_forest.white)
                            text2 = screen.blit(text2, (600, 550))
                        elif user_text == "y":
                            text2 = font.render(
                                'Wrong! Press "3" for next!', True, Learn_forest.red)
                            text2 = screen.blit(text2, (600, 550))
                        else:
                            user_text = user_text[:-1]
                    pygame.draw.rect(screen, color, input_rect)
                    text_surface = base_font.render(
                        user_text, True, (255, 255, 255))
                    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, text_surface.get_width()+10)
                    pygame.display.flip()
                    pygame.time.Clock().tick(60)
            pygame.display.update()
            pygame.display.flip()


if __name__ == '__main__':
    Learn_forest().run()
