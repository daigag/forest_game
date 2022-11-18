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
        self.background_image = None
        self.running = True

    def main_background(self):

        # self.background_image = pygame.image.load('vasaras_bg.jpg')
        # background_image = pygame.transform.scale(
        #     self.background_image, (screen_width, screen_height))
        # background_image_rectangle = background_image.get_rect()
        # screen.blit(background_image, background_image_rectangle)

        self.intro = Text('Welcome to the Forest Game!', (200, 50)).draw()
        memory_game_image = pygame.image.load(
            "forest_buttons/memory_game.png")
        memory_game_image = pygame.transform.scale(
            memory_game_image, (2500, 900))
        hide_and_seek_image = pygame.image.load(
            "forest_buttons/Hide_and_seek.png")
        hide_and_seek_image = pygame.transform.scale(
            hide_and_seek_image, (2500, 900))
        learn_forest_image = pygame.image.load(
            "forest_buttons/Forest_game.png")
        learn_forest_image = pygame.transform.scale(
            learn_forest_image, (2500, 900))
        self.memory_game_button = Button(
            325, 100, memory_game_image, 1).draw()
        self.learn_forest_button = Button(
            325, 275, hide_and_seek_image, 1).draw()
        self.learn_forest1_button = Button(
            325, 450, learn_forest_image, 1).draw()

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
