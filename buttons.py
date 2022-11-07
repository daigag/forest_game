import pygame
import button

pygame.init()
screen_width = 1000
screen_height = 600
black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("She goes Tech project by Daiga and Zane :)")

memory_game_image = pygame.image.load('button1.png').convert_alpha()
learn_forest_image = pygame.image.load('button2.png').convert_alpha()


# button instances (how far in, how low, ..., size)
memory_game_button = button.Button(300, 200, memory_game_image, 0.8)
learn_forest_button = button.Button(600, 200, learn_forest_image, 0.8)


running = True
while running:

    screen.fill(black)

    if memory_game_button.draw(screen):
        print("Memory Game")

    if learn_forest_button.draw(screen):
        print("Learn forest")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    pygame.display.update()

pygame.quit()
exit()
