import pygame, os, random
from pygame.locals import *
from sound import *

screen = pygame.display.set_mode((1000, 600))

green = (0, 50, 0)

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
    
    winter_img = pygame.image.load("ziemas_bg.jpg")
    winter_img = pygame.transform.scale(winter_img, (1000, 600))

    pointer = Pointer()
    pointer_group = pygame.sprite.Group()
    pointer_group.add(pointer)

    # Object
    object_group = pygame.sprite.Group()
    for Object.target in range(20):
        new_target = Object(random.randrange(0, 1000),
                            random.randrange(0, 600))
        object_group.add(new_target)

    def __init__(self):
        pygame.init()
        self.running = True
     
    def run(self):

        pygame.display.set_caption('Hide and seek')
        icon = pygame.image.load('citi_atteli/a fly agaric.png')
        icon = pygame.display.set_icon(icon)

        background = screen.blit(Hide_and_seek.winter_img, (0, 0))
        background

        pygame.display.update()

        Hide_and_seek.pointer_group.draw(screen)
        Hide_and_seek.pointer_group.update()
        pygame.display.flip()

        Hide_and_seek.object_group.draw(screen)
        Hide_and_seek.pointer_group.draw(screen)
        Hide_and_seek.pointer_group.update()

        for self.target in range(20):
            new_target = Object(random.randrange(
                0, 1000), random.randrange(0, 600))
            Hide_and_seek.object_group.add(new_target)

        pygame.mouse.set_visible(False)


        while True:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.type == K_ESCAPE:
                        pygame.display.quit()
                        self.running = False
                        screen.fill(green)
                        pygame.display.set_caption('Forest Game by Zane and Daiga')
                        icon = pygame.image.load('citi_atteli/a pine needle.png')
                        icon = pygame.display.set_icon(icon)
                        return
            
                elif event.type == MOUSEBUTTONDOWN:
                    Pointer().klick()

                screen.blit(Hide_and_seek.winter_img, (0, 0))
                Hide_and_seek.object_group.draw(screen)
                Hide_and_seek.pointer_group.draw(screen)
                Hide_and_seek.pointer_group.update()
            pygame.display.flip()
            pygame.display.update()


if __name__ == '__main__':
    Hide_and_seek().run()
