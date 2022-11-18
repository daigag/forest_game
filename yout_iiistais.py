import pygame, random, os, sys, csv, time
from pygame.locals import *
from pygame import mixer
from gtts import gTTS

#colors
green = (1, 68, 33)
black = (0, 0, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128)

#background_images
winter_image = pygame.image.load("ziemas_bg.jpg")
winter_image = pygame.transform.scale(winter_image, (1000, 600))
summer_image = pygame.image.load("vasaras_bg.jpg")
summer_image = pygame.transform.scale(summer_image, (1000, 600)) 

#set screen
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

#menu screen
background = screen.fill(green)
game_name = pygame.display.set_caption('Forest Game')
game_icon = pygame.image.load('citi_atteli/skuja.png')
game_icon = pygame.display.set_icon(game_icon)

#set clock
timer = pygame.time.Clock()
fps = 60

class Player:
    pass


def text_on_button():
    with open ('learn_forest_data/input_data.csv', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0
        if line_count == 0:
            for row in reader:
                line_count += 1
            #print(f'You see the {row[3]}, in latvian - {row[2]}.')
            print(f'{row[2]}')
                #line_count += 1
        #print(f'Processed {line_count} lines.')
        
text = str(text_on_button())


class Read_loud:
    # PART 1
    def say(text, filename="temp.mp3", delete_audio_file=True, language="en", slow=False):
        # PART 2
        audio = gTTS(text, lang=language, slow=slow)
        audio.save(filename)

        if os.name == "posix":
            sound = AudioSegment.from_mp3(filename)
            old_filename = filename
            filename = filename.split(".")[0] + ".ogg"
            sound.export(filename, format="ogg")
            if delete_audio_file:
                os.remove(old_filename)

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
        
Read_loud.say("Welcome to the forest!")


class Textx:
    pass

class Text:
    def text():
        font1 = pygame.font.SysFont('calibri', 50)
        font2 = pygame.font.SysFont('calibri', 30)
        text1 = font1.render('Welcome to the forest!', False, white) 
        text2 = font2.render('Press "w" for winter forest, press "s" for summer forest!', False, white)
        text1 = screen.blit(text1, (30, 20))
        text2 = screen.blit(text2, (30, 70))
        return text1, text2

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * 0.15), int(height*0.15)))
        self.scale = scale
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

class Memory_game:
    #set tiles
    picture_size = 90
    columns = 6
    rows = 6
    left_margin = (width - ((picture_size + 8) * columns)) // 2
    right_margin = left_margin
    top_margin = (height - ((picture_size + 8) * rows)) // 2
    bottom_margin = top_margin

    #set score counting variables
    first_guess = None
    second_guess = None
    #font = pygame.font.Font('freesansbold.ttf', 22)
    score = 0
    pictures_for_game = []
    pictures_in_memory = []
    pictures_in_memory_rectangle = []
    hidden_pictures = []
    
    def make_background():
        pygame.display.set_caption("Memory game - forest and animals")
        game_icon = pygame.image.load('memory_game/output-onlinepngtools (1).png')
        pygame.display.set_icon(game_icon)
        background_image = pygame.image.load('ziemas_bg.jpg')
        background_image = pygame.transform.scale(background_image, (width, height))
        background_image_rectangle = background_image.get_rect()
        screen.blit(background_image, background_image_rectangle)
        #score_text = Memory_game.font.render((f'Current turns: {Memory_game.score //2 }'), True, white)
        #screen.blit(score_text, (800, 300))
    
    def __init__(self):
        #pygame.init()
        self.running = True

    def creating_tiles():
        for item in os.listdir('memory_game/'): # creating list of pictures
            Memory_game.pictures_for_game.append(item.split('.')[0]) # adding pictures to list
        copy_of_pictures_for_game = Memory_game.pictures_for_game.copy() # creating copy of list
        Memory_game.pictures_for_game.extend(copy_of_pictures_for_game) # adding copy of list to list
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
     
        while self.run:   
            timer.tick(fps)         
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for item in Memory_game.pictures_in_memory_rectangle:
                        if item.collidepoint(event.pos):
                            if Memory_game.hidden_pictures[Memory_game.pictures_in_memory_rectangle.index(item)] != True:
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
                running = False

        pygame.display.update()
        pygame.display.flip()
        pygame.quit()

class Learn_forest:
    def __init__(self):
        self.running = True
    
    def forest_animal_image():
        animal = random.choice(os.listdir('meza_dzivnieki')) # choose random image from folder
        animal_image = pygame.image.load(os.path.join('meza_dzivnieki', animal)).convert() # if convert - with white background, if without - without background
        animal_image = pygame.transform.scale(animal_image, (300, 300)) # resize image
        animal_image = screen.blit(animal_image, (350,150)) # draw image on screen
        animal_file_name = os.path.splitext(str(animal))[0] # get file name without extension
        f_font = pygame.font.SysFont('comicsansms', 30)
        f_text = f_font.render(animal_file_name, True, white) # text, antialiasing, color
        f_text = screen.blit(f_text, (450, 450))    
        return animal_image, f_text
      
    def other_forest_things():
        other = random.choice(os.listdir('citi_atteli')) # choose random image from folder
        other_image = pygame.image.load(os.path.join('citi_atteli', other)).convert() # load image
        other_image = pygame.transform.scale(other_image, (300, 350)) # resize image
        other_image = screen.blit(other_image, (350,100)) # draw image on screen
        return other_image
    
    def image_file_name():
        image_file_name.font = pygame.font.SysFont('comicsansms', 20)
        image_file_name = image_file_name.font.render(os.path.splitext(str(Main.other_forest_things()))[0], True, black) # text, antialiasing, color
        image_file_name = screen.blit(image_file_name, (350, 200))
        return image_file_name
    
    def run(self):
        Memory_game.make_background()
        # while self.running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #             if Learn_forest.forest_animal_image().collidepoint(event.pos):
        #                 print('yes')
        #             else:
        #                 print('no')
    
    
  
class Main:
    def __init__(self):
        pygame.init()
        self.running = True
             
    def run(self): 
        while self.running:
            self.intro = Text.text()
            memory_game_image = pygame.image.load("forest_buttons/memory_eng.png").convert_alpha()
            learn_forest_image = pygame.image.load("forest_buttons/learnforest_eng.png").convert_alpha()
            self.memory_game_button = Button(30, 120, memory_game_image, 1).draw()
            self.learn_forest_button = Button(30, 220, learn_forest_image, 1).draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if self.memory_game_button:
                    Memory_game().run()
                if self.learn_forest_button:
                    Learn_forest().run()
                elif event.type == KEYDOWN:
                    if event.key == K_w:
                        self.background = screen.blit(winter_image, (0, 0))
                    elif event.key == K_s:
                        self.background = screen.blit(summer_image, (0, 0)) 
                pygame.display.flip()
        pygame.quit()
    
if __name__ == '__main__':
    Main().run()