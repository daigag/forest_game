
from text import Text
from learn_forest import Learn_forest
from hide_and_seek import Hide_and_seek
from memory_game import Memory_game
from button import Button
from pygame import mixer
from pygame.locals import *
import pygame
from sound import Read_loud

pygame.init()
mixer.init()

# colours
white = (255, 255, 255)
black = (0, 0, 0)
green = (1, 68, 33)
teal = (0, 128, 128)
red = (255, 0, 0)
gray = (128, 128, 128)

# clock
timer = pygame.time.Clock()
fps = 60

# main screen
screen = pygame.display.set_mode((1000, 600))
background = screen.fill(green)
title = pygame.display.set_caption('Forest Game by Zane and Daiga')
icon = pygame.image.load('citi_atteli/skuja.png')
icon = pygame.display.set_icon(icon)
screen_width = screen.get_width()
screen_height = screen.get_height()
screen_width = 1000
screen_height = 600

# background images
winter_img = pygame.image.load("ziemas_bg.jpg")
winter_img = pygame.transform.scale(winter_img, (1000, 600))
summer_img = pygame.image.load("vasaras_bg.jpg")
summer_img = pygame.transform.scale(summer_img, (1000, 600))

pygame.font.get_fonts()


class Main():

    def __init__(self):
        pygame.init()
        self.background_image = None
        self.running = True

    def main_background(self):

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
        self.hide_and_seek_button = Button(
            325, 275, hide_and_seek_image, 1).draw()
        self.learn_forest_button = Button(
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
                if self.hide_and_seek_button:
                    Read_loud.say('Hide and Seek')
                    Hide_and_seek().run()
                if self.learn_forest_button:
                    Read_loud.say('Learn forest')
                    Learn_forest().run()
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    Main().run()
