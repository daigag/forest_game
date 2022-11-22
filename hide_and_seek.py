
import os
import pygame
from pygame import mixer
from sound import Read_loud
import random

mixer.init()

screen_width = 1000
screen_height = 600
# background images
winter_img = pygame.image.load("ziemas_bg.jpg")
winter_img = pygame.transform.scale(winter_img, (1000, 600))
summer_img = pygame.image.load("vasaras_bg.jpg")
summer_img = pygame.transform.scale(summer_img, (1000, 600))
screen = pygame.display.set_mode((1000, 600))
pygame.font.get_fonts()


class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('forest_buttons/pointer_2.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.catch = pygame.mixer.Sound('sounds/win.wav')

    def klick(self):
        self.catch.play()
        pygame.sprite.spritecollide(
            Hide_and_seek.pointer, Hide_and_seek.object_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Object(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = random.choice(os.listdir('meza_dzivnieki'))
        self.image = pygame.image.load(
            os.path.join('meza_dzivnieki', self.image))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


class Hide_and_seek:

    pointer = Pointer()
    pointer_group = pygame.sprite.Group()
    pointer_group.add(pointer)

    # Object
    object_group = pygame.sprite.Group()
    for Object.target in range(20):
        new_target = Object(random.randrange(0, screen_width),
                            random.randrange(0, screen_height))
        object_group.add(new_target)

    def __init__(self):
        pygame.init()
        self.running = True

        screen.blit(summer_img, (0, 0))
        pygame.display.update()

        Hide_and_seek.pointer_group.draw(screen)
        Hide_and_seek.pointer_group.update()
        pygame.display.flip()

        Hide_and_seek.object_group.draw(screen)
        Hide_and_seek.pointer_group.draw(screen)
        Hide_and_seek.pointer_group.update()

        for self.target in range(20):
            new_target = Object(random.randrange(
                0, screen_width), random.randrange(0, screen_height))
            Hide_and_seek.object_group.add(new_target)

        pygame.mouse.set_visible(False)

    def run(self):

        while True:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(green)
                    Main().run()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Pointer().klick()

                # if event.type == pygame.KEYDOWN:
                #     button_press_time = pygame.time.get_ticks()
                #     screen.fill((255,255,255))

            # current_time = pygame.time.get_ticks()
            # if current_time - button_press_time > 2000:
            #     screen.fill((0,0,0))
            # print(f"current_time {current_time} button_press time: {button_press_time}")

            screen.blit(summer_img, (0, 0))
            Hide_and_seek.object_group.draw(screen)
            Hide_and_seek.pointer_group.draw(screen)
            Hide_and_seek.pointer_group.update()
            pygame.display.flip()


if __name__ == '__main__':
    Hide_and_seek().run()
