
import pygame
import random
import os
import sys
import csv
import time
from pygame.locals import *
from pygame import mixer
from gtts import gTTS
from deep_translator import GoogleTranslator
import pygame_textinput
import Text_games

# color variables
green = (1, 68, 33)
black = (0, 0, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128)

# clock
timer = pygame.time.Clock()
fps = 60

# background images
winter_img = pygame.image.load("ziemas_bg.jpg")
winter_img = pygame.transform.scale(winter_img, (1000, 600))
summer_img = pygame.image.load("vasaras_bg.jpg")
summer_img = pygame.transform.scale(summer_img, (1000, 600))

# main screen
screen = pygame.display.set_mode((1000, 600))
background = screen.fill(green)
title = pygame.display.set_caption('Forest Game by Zane and Daiga')
icon = pygame.image.load('citi_atteli/skuja.png')
icon = pygame.display.set_icon(icon)

pygame.font.get_fonts()

screen_width = screen.get_width()
screen_height = screen.get_height()


class Learn_forest:
    def __init__(self):
        pygame.init()
        self.running = True

        screen.blit(summer_img, (0, 0))
        pygame.display.update()

    def forest_from_csv():
        file = open('learn_forest_data/input_data.csv', encoding="utf8")
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

    def forest_animal_image():
        # choose random image from folder
        animal = random.choice(os.listdir('meza_dzivnieki'))
        # if convert - with white background, if without - without background
        animal_image = pygame.image.load(
            os.path.join('meza_dzivnieki', animal)).convert()
        animal_image = pygame.transform.scale(
            animal_image, (300, 300))  # resize image
        animal_image = screen.blit(
            animal_image, (350, 150))  # draw image on screen
        # get file name without extension
        animal_file_name = os.path.splitext(str(animal))[0]
        f_font = pygame.font.SysFont('comicsansms', 30)
        # text, antialiasing, color
        f_text = f_font.render(animal_file_name, True, white)
        f_text = screen.blit(f_text, (450, 450))
        # read_animal = Read_loud.say(f'Tas ir {animal_file_name}')
        translated_animal_f = GoogleTranslator(
            source='auto', target='en').translate(animal_file_name)
        translated_lt = GoogleTranslator(
            source='auto', target='lt').translate(animal_file_name)
        translated_animal_f = str(translated_animal_f)
        translated_lt = str(translated_lt)
        translated_animal = f_font.render(translated_animal_f, True, white)
        translated_an_lt = f_font.render(translated_lt, True, white)
        translated_animal = screen.blit(translated_animal, (450, 500))
        translated_an_lt = screen.blit(translated_an_lt, (450, 550))
        read_translated_animal = Read_loud.say(
            f'This is {translated_animal_f}.')
        return animal_image, translated_animal, read_translated_animal

    def other_forest_things():
        # choose random image from folder
        other = random.choice(os.listdir('memory_game/atteli'))
        other_image = pygame.image.load(os.path.join(
            'memory_game/atteli', other)).convert()  # load image
        other_image = pygame.transform.scale(
            other_image, (300, 350))  # resize image
        other_image = screen.blit(
            other_image, (350, 100))  # draw image on screen
        return other_image

    def what_is_it():
        #animal_image = Learn_forest.forest_animal_image().animal_image
        text = Text('What is it?', (150, 50)).draw()
        # choose random image from folder
        animal = random.choice(os.listdir('meza_dzivnieki'))
        # if convert - with white background, if without - without background
        animal_image = pygame.image.load(
            os.path.join('meza_dzivnieki', animal)).convert()
        animal_image = pygame.transform.scale(
            animal_image, (300, 300))  # resize image
        animal_image = screen.blit(
            animal_image, (350, 150))  # draw image on screen
        animal_file_name = os.path.splitext(str(animal))[0]
        base_font = pygame.font.Font(None, 32)

        return text, animal_image, user_text

    # Feed it with events every frame

    # Blit its surface onto the screen

    def run(self):

        pygame.init()
        mixer.init()
        mixer.music.load('sounds/forest_summer.wav')
        mixer.music.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(green)
                    Main().run()

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.key.set_repeat()
                        screen.blit(summer_img, (0, 0))
                        pygame.display.update()
                        Learn_forest.forest_animal_image()
                    elif event.key == K_d:
                        pygame.key.set_repeat()
                        screen.blit(summer_img, (0, 0))
                        pygame.display.update()
                        Learn_forest.what_is_it()
                    elif event.key == K_a:
                        Input.game_intro()
                    else:
                        pass

            pygame.display.update()
            pygame.display.flip()


class Read_loud:
    # PART 1
    def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
        # PART 2
        audio = gTTS(text, lang=language, slow=slow)
        audio.save(filename)

        # PART 3
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()

        # PART 4
        seconds = 0
        while mixer.music.get_busy() == 1:
            time.sleep(0.25)
            seconds += 0.25

        # PART 5
        mixer.quit()
        if delete_audio_file:
            os.remove(filename)
        print(f"audio file played for {seconds} seconds")
