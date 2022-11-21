
from Text_games import *
from Learn_forest import *
from Hide_and_seek import *
from memory_game import *
from button import *
from pygame import mixer
from pygame.locals import *
import pygame

pygame.init()
mixer.init()


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
