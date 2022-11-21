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
from memory_game import *
from Hide_and_seek import *
from Learn_forest import *
from Button import *

pygame.init()
mixer.init()

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


class Player:
    pass


class Input:
    def __init__(self):
        pygame.display.update()
        self.running = True

    def text1(word, x, y):
        font = pygame.font.SysFont(None, 25)
        text = font.render("{}".format(word), True, red)
        return screen.blit(text, (x, y))

    def inpt():
        word = ""
        # example asking name
        Input.text1(f"Please enter your name:{input} ", 300, 400)
        pygame.display.flip()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        word += str(chr(event.key))
                    if event.key == pygame.K_b:
                        word += chr(event.key)
                    if event.key == pygame.K_c:
                        word += chr(event.key)
                    if event.key == pygame.K_d:
                        word += chr(event.key)
                    if event.key == pygame.K_RETURN:
                        done = False
                    # events...
        return Input.text1(word, 700, 30)

    def game_intro():
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        intro = False
            Input.inpt()  # Here we are calling our function
            screen.fill(white)

            pygame.display.update()
            timer.tick(15)

    def run(self):
        self.game_intro()


class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 60
        self.fontcolor = Color('white')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        screen.blit(self.img, self.rect)


# class Read_loud:
#     # PART 1
#     def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
#         # PART 2
#         audio = gTTS(text, lang=language, slow=slow)
#         audio.save(filename)

#         # if os.name == "posix":
#         #     sound = AudioSegment.from_mp3(filename)
#         #     old_filename = filename
#         #     filename = filename.split(".")[0] + ".ogg"
#         #     sound.export(filename, format="ogg")
#         #     if delete_audio_file:
#         #         os.remove(old_filename)

#         # PART 3
#         mixer.init()
#         mixer.music.load(filename)
#         mixer.music.play()

#         # PART 4
#         seconds = 0
#         while mixer.music.get_busy() == 1:
#             time.sleep(0.25)
#             seconds += 0.25

#         # PART 5
#         mixer.quit()
#         if delete_audio_file:
#             os.remove(filename)
#         print(f"audio file played for {seconds} seconds")

class Main():

    def __init__(self):
        pygame.init()
        self.running = True

    def make_background():
        pygame.display.set_caption("Memory game - forest and animals")
        game_icon = pygame.image.load(
            'memory_game/output-onlinepngtools (1).png')
        pygame.display.set_icon(game_icon)
        background_image = pygame.image.load('ziemas_bg.jpg')
        background_image = pygame.transform.scale(
            background_image, (screen_width, screen_height))
        background_image_rectangle = background_image.get_rect()
        screen.blit(background_image, background_image_rectangle)
        score_text = Memory_game.font.render(
            f'Current turns: {Memory_game.score //2 }', True, white)
        screen.blit(score_text, (800, 300))

    def creating_tiles():
        for item in os.listdir('memory_game/'):  # creating list of pictures
            Memory_game.pictures_for_game.append(
                item.split('.')[0])  # adding pictures to list
        copy_of_pictures_for_game = Memory_game.pictures_for_game.copy()  # creating copy of list
        Memory_game.pictures_for_game.extend(
            copy_of_pictures_for_game)  # adding copy of list to list
        copy_of_pictures_for_game.clear()
        random.shuffle(Memory_game.pictures_for_game)

        for item in Memory_game.pictures_for_game:
            picture = pygame.image.load(f'memory_game/{item}.png')
            picture = pygame.transform.scale(
                picture, (Memory_game.picture_size, Memory_game.picture_size))
            Memory_game.pictures_in_memory.append(picture)
            picture_rectangles = picture.get_rect()
            Memory_game.pictures_in_memory_rectangle.append(picture_rectangles)

        for i in range(len(Memory_game.pictures_in_memory_rectangle)):
            Memory_game.pictures_in_memory_rectangle[i][0] = Memory_game.left_margin + \
                ((Memory_game.picture_size + 8) * (i // Memory_game.columns))
            Memory_game.pictures_in_memory_rectangle[i][1] = Memory_game.top_margin + \
                ((Memory_game.picture_size + 8) * (i % Memory_game.rows))
            Memory_game.hidden_pictures.append(False)

    def run(self):
        first_guess = Memory_game.first_guess
        second_guess = Memory_game.second_guess
        score = Memory_game.score
        Memory_game.make_background()
        Memory_game.creating_tiles()
        mixer.init()
        mixer.music.load('sounds/forest_summer.wav')
        mixer.music.play()

        while self.run:
            timer.tick(fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.display.quit(), sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for item in Memory_game.pictures_in_memory_rectangle:
                        if item.collidepoint(event.pos):
                            if Memory_game.hidden_pictures[Memory_game.pictures_in_memory_rectangle.index(item)] != True:
                                score = Memory_game.score
                                if first_guess != None:
                                    second_guess = Memory_game.pictures_in_memory_rectangle.index(
                                        item)
                                    Memory_game.hidden_pictures[second_guess] = True
                                    score += 1
                                else:
                                    first_guess = Memory_game.pictures_in_memory_rectangle.index(
                                        item)
                                    Memory_game.hidden_pictures[first_guess] = True
                                    score += 1

            for i in range(len(Memory_game.pictures_for_game)):
                if Memory_game.hidden_pictures[i] == True:
                    screen.blit(
                        Memory_game.pictures_in_memory[i], Memory_game.pictures_in_memory_rectangle[i])
                else:
                    pygame.draw.rect(
                        screen, white, (Memory_game.pictures_in_memory_rectangle[i][0], Memory_game.pictures_in_memory_rectangle[i][1], Memory_game.picture_size, Memory_game.picture_size))
            pygame.display.update()

            if first_guess != None and second_guess != None:
                if Memory_game.pictures_for_game[first_guess] == Memory_game.pictures_for_game[second_guess]:
                    first_guess, second_guess = None, None
                else:
                    pygame.time.wait(1000)
                    Memory_game.hidden_pictures[first_guess] = False
                    Memory_game.hidden_pictures[second_guess] = False
                    first_guess, second_guess = None, None

            win = 1
            for number in range(len(Memory_game.hidden_pictures)):
                win *= Memory_game.hidden_pictures[number]

            if win == 1:
                self.running = False

        pygame.display.update()
        pygame.display.flip()


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


class Main:
    def __init__(self):
        pygame.init()
        self.running = True

    def main_background(self):

        # self.background_image = pygame.image.load('vasaras_bg.jpg')
        # background_image = pygame.transform.scale(
        #     self.background_image, (screen_width, screen_height))
        # background_image_rectangle = background_image.get_rect()
        # screen.blit(background_image, background_image_rectangle)

        self.intro = Text('Welcome to the Forest Game!', (200, 50)).draw()
        memory_game_image = pygame.image.load(
            "meza_dzivnieki/vilks.png").convert_alpha()
        learn_forest_image = pygame.image.load(
            "meza_dzivnieki/lapsa.png").convert_alpha()
        learn_forest_image1 = pygame.image.load(
            "meza_dzivnieki/lācis.png").convert_alpha()
        self.memory_game_button = Button(200, 250, memory_game_image, 1).draw()
        self.learn_forest_button = Button(
            500, 250, learn_forest_image, 1).draw()
        self.learn_forest1_button = Button(
            800, 250, learn_forest_image1, 1).draw()

    def run(self):

        while self.running:
            Main.main_background(self)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if self.memory_game_button:
                    Read_loud.say('Memory game')
                    Memory_game().run()
                if self.learn_forest_button:
                    Read_loud.say('Hide and Seek')
                    Hide_and_seek().run()
                if self.learn_forest1_button:
                    Read_loud.say('Learn forest')
                    Learn_forest().run()
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    Main().run()
