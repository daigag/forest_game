import pygame
import os
import random

pygame.init()

timer = pygame.time.Clock()
fps = 60
screen_width = 1000
screen_height = 600
picture_size = 90
columns = 6
rows = 6
left_margin = (screen_width - ((picture_size + 8) * columns)) // 2
right_margin = left_margin
top_margin = (screen_height - ((picture_size + 8) * rows)) // 2
bottom_margin = top_margin
white = (255, 255, 255)
black = (0, 0, 0)
first_guess = None
second_guess = None
font = pygame.font.Font('freesansbold.ttf', 22)
screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
pictures_for_game = []
pictures_in_memory = []
pictures_in_memory_rectangle = []
hidden_pictures = []


class Memory_game:
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
        Memory_game.score_text = font.render(f'Current turns: {score //2 }', True, white)
        screen.blit(Memory_game.score_text, (800, 300))

    def creating_tiles():
        for item in os.listdir('memory_game/'): # creating list of pictures
            pictures_for_game.append(item.split('.')[0]) # adding pictures to list
        copy_of_pictures_for_game = pictures_for_game.copy() # creating copy of list
        pictures_for_game.extend(copy_of_pictures_for_game) # adding copy of list to list
        copy_of_pictures_for_game.clear()
        random.shuffle(pictures_for_game)

        for item in pictures_for_game:
            picture = pygame.image.load(f'memory_game/{item}.png')
            picture = pygame.transform.scale(
                picture, (picture_size, picture_size))
            pictures_in_memory.append(picture)
            picture_rectangles = picture.get_rect()
            pictures_in_memory_rectangle.append(picture_rectangles)

        for i in range(len(pictures_in_memory_rectangle)):
            pictures_in_memory_rectangle[i][0] = left_margin + \
                ((picture_size + 8) * (i // columns))
            pictures_in_memory_rectangle[i][1] = top_margin + \
                ((picture_size + 8) * (i % rows))
            hidden_pictures.append(False)

    def run(self):
        global first_guess
        global second_guess
        global score

        while self.run:
            timer.tick(fps)
            Memory_game.make_background()
            Memory_game.creating_tiles()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit(), sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for item in pictures_in_memory_rectangle:
                        if item.collidepoint(event.pos):
                            if hidden_pictures[pictures_in_memory_rectangle.index(item)] != True:
                                if first_guess != None:
                                    second_guess = pictures_in_memory_rectangle.index(
                                        item)
                                    hidden_pictures[second_guess] = True
                                    score += 1
                                else:
                                    first_guess = pictures_in_memory_rectangle.index(
                                        item)
                                    hidden_pictures[first_guess] = True
                                    score += 1

            for i in range(len(pictures_for_game)):
                if hidden_pictures[i] == True:
                    screen.blit(
                        pictures_in_memory[i], pictures_in_memory_rectangle[i])
                else:
                    pygame.draw.rect(
                        screen, white, (pictures_in_memory_rectangle[i][0], pictures_in_memory_rectangle[i][1], picture_size, picture_size))
            pygame.display.update()

            if first_guess != None and second_guess != None:
                if pictures_for_game[first_guess] == pictures_for_game[second_guess]:
                    first_guess, second_guess = None, None
                else:
                    pygame.time.wait(1000)
                    hidden_pictures[first_guess] = False
                    hidden_pictures[second_guess] = False
                    first_guess, second_guess = None, None

            win = 1
            for number in range(len(hidden_pictures)):
                win *= hidden_pictures[number]

            if win == 1:
                running = False

        pygame.display.update()
        pygame.display.flip()

    # pygame.quit()


if __name__ == '__main__':
    Memory_game().run()
