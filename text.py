import pygame

screen = pygame.display.set_mode((1000, 600))

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 60
        self.fontcolor = (255, 255, 255)
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
