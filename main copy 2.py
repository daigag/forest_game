import pygame, random, os, sys, csv, time
from pygame.locals import *
from pygame import mixer
from gtts import gTTS

pygame.init()
mixer.init()

#color variables
green = (1, 68, 33)
black = (0, 0, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (128, 128, 128)

timer = pygame.time.Clock()
fps = 60

#bg images
winter_img = pygame.image.load("ziemas_bg.jpg")
winter_img = pygame.transform.scale(winter_img, (1000, 600))
summer_img = pygame.image.load("vasaras_bg.jpg")
summer_img = pygame.transform.scale(summer_img, (1000, 600)) 

#main screen
screen = pygame.display.set_mode((1000, 600))
bg = screen.fill(green)
title = pygame.display.set_caption('Lielā dabas spēle "Mežs"')
icon = pygame.image.load('citi_atteli/skuja.png')
icon = pygame.display.set_icon(icon)

pygame.font.get_fonts()

screen_width = screen.get_width()
screen_height = screen.get_height()

class Player:
    pass

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


# with open ('learn_forest_data/input_data.csv', encoding="utf-8") as file:
#     reader = csv.reader(file, delimiter=',')
#     line_count = 0
#     for row in reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             Read_loud.say(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             Read_loud.say(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             # image = pygame.image.load(f'meza_dzivnieki/{row[1]}')
#             # image = pygame.transform.scale(image, (50, 50))
#             # show_image = True
#             line_count += 1
#     print(f'Processed {line_count} lines.')
    
# #text = f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.'

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
  
class Text_button():
    def __init__(self, color, x , y , width , height , text='', textSize = 40):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textSize = textSize 

    def draw(self,win,outline= None):
        self.running = True

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
            #self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1.1), int(self.image.get_height()*1.1)))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True 
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

class Crosshair(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('forest_buttons/pointer_2.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        mixer.init()
        self.gunshot = pygame.mixer.Sound('sounds/win.wav')
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(Crosshair_game.crosshair, Crosshair_game.target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.image = random.choice(os.listdir('meza_dzivnieki')) 
        self.image = pygame.image.load(os.path.join('meza_dzivnieki', self.image)) 
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        
class Crosshair_game:
    
    # crosshair = Crosshair()
    # crosshair_group = pygame.sprite.Group()
    # crosshair_group.add(crosshair)

    # #Target
    # target_group = pygame.sprite.Group()
    # for Target.target in range(20):
    #     new_target = Target(random.randrange(0,screen_width), random.randrange(0,screen_height))
    #     target_group.add(new_target)
    
    # def screen_cg():
    #     pygame.display.set_caption("Memory game - forest and animals")
    #     game_icon = pygame.image.load(
    #         'memory_game/output-onlinepngtools (1).png')
    #     pygame.display.set_icon(game_icon)
    #     background_image = pygame.image.load('ziemas_bg.jpg')
    #     background_image = pygame.transform.scale(
    #         background_image, (screen_width, screen_height))
    #     background_image_rectangle = background_image.get_rect()
    #     screen.blit(background_image, background_image_rectangle)
    #     score_text = Memory_game.font.render(f'Current turns: {Memory_game.score //2 }', True, white)
    #     screen.blit(score_text, (800, 300))
    #     pygame.mouse.set_visible(False)
        
   
    def __init__(self):
        pygame.init()
        self.running = True
        
       
    def run(self):
        Memory_game.make_background()
        # self.crosshair = Crosshair()
      
        # Crosshair_game.crosshair_group.draw(screen)
        # Crosshair_game.crosshair_group.update()
        # pygame.display.flip()  
    
      
        # Crosshair_game.target_group.draw(screen)
        # Crosshair_game.crosshair_group.draw(screen)
        # Crosshair_game.crosshair_group.update()

        # for self.target in range(20):
        #     new_target = Target(random.randrange(0,screen_width), random.randrange(0,screen_height))
        #     Crosshair_game.target_group.add(new_target)
    
#     def __init__(self):
#         pygame.init()
#         self.running = True
    
    
#     def run(self):
#              #Target
#         # pygame.display.set_caption("Memory game - forest and animals")
#         # game_icon = pygame.image.load(
#         #     'memory_game/output-onlinepngtools (1).png')
#         # pygame.display.set_icon(game_icon)


#         while True:
           
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit() 
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     crosshair.shoot()
#                 # if event.type == pygame.KEYDOWN:
#                 #     button_press_time = pygame.time.get_ticks()
#                 #     screen.fill((255,255,255))
                    
#             # current_time = pygame.time.get_ticks()
#             # if current_time - button_press_time > 2000:
#             #     screen.fill((0,0,0))
#             # print(f"current_time {current_time} button_press time: {button_press_time}")
            

#             screen.blit(background,(0,0))
#             target_group.draw(screen)
#             crosshair_group.draw(screen)
#             crosshair_group.update()
#             pygame.display.flip()

class Memory_game:
    picture_size = 90
    columns = 6
    rows = 6
    left_margin = (screen_width - ((picture_size + 8) * columns)) // 2
    right_margin = left_margin
    top_margin = (screen_height - ((picture_size + 8) * rows)) // 2
    bottom_margin = top_margin
    first_guess = None
    second_guess = None
    font = pygame.font.Font('freesansbold.ttf', 22)
    score = 0
    pictures_for_game = []
    pictures_in_memory = []
    pictures_in_memory_rectangle = []
    hidden_pictures = []

   
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
        score_text = Memory_game.font.render(f'Current turns: {Memory_game.score //2 }', True, white)
        screen.blit(score_text, (800, 300))

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
    
    def forest_from_csv():
        file = open('learn_forest_data/input_data.csv', encoding="utf8")
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()
    
    def forest_animal_image():
        animal = random.choice(os.listdir('meza_dzivnieki')) # choose random image from folder
        animal_image = pygame.image.load(os.path.join('meza_dzivnieki', animal)).convert() # if convert - with white bg, if without - without bg
        animal_image = pygame.transform.scale(animal_image, (300, 300)) # resize image
        animal_image = screen.blit(animal_image, (350,150)) # draw image on screen
        animal_file_name = os.path.splitext(str(animal))[0] # get file name without extension
        f_font = pygame.font.SysFont('comicsansms', 30)
        f_text = f_font.render(animal_file_name, True, white) # text, antialiasing, color
        f_text = screen.blit(f_text, (450, 450))    
        return animal_image, f_text
      
    def other_forest_things():
        other = random.choice(os.listdir('memory_game/atteli')) # choose random image from folder
        other_image = pygame.image.load(os.path.join('memory_game/atteli', other)).convert() # load image
        other_image = pygame.transform.scale(other_image, (300, 350)) # resize image
        other_image = screen.blit(other_image, (350,100)) # draw image on screen
        return other_image
    
    def image_file_name():
        image_file_name.font = pygame.font.SysFont('comicsansms', 20)
        image_file_name = image_file_name.font.render(os.path.splitext(str(Main.other_forest_things()))[0], True, black) # text, antialiasing, color
        image_file_name = screen.blit(image_file_name, (350, 200))
        return image_file_name
    
    def forest_animal_sound():
        animal_c = random.choice(os.listdir(Learn_forest.forest_from_csv().file))
        animal_image_c = pygame.image.load(os.path.join('meza_dzivnieki', animal_c)).convert() # if convert - with white background, if without - without background
        animal_image_c = pygame.transform.scale(animal_image_c, (100, 100))
        animal_image_c = screen.blit(animal_image_c, (350,150))
        animal_file_name_c = animal_c, column = 'Latvian'
        text = animal_c[animal_c][1]
        return text
    
    
    
    def run(self):



        screen.fill(teal)
        Memory_game.creating_tiles()
        mixer.init()
        mixer.music.load('sounds/forest_summer.wav')
        mixer.music.play()   
        Learn_forest.forest_animal_image()     

        while self.run:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    for item in Learn_forest.forest_animal_image():
                        if item.collidepoint(event.pos):
                            if Learn_forest.forest_animal_image() != True:
                                screen.blit()
                                pygame.update.screen()
                                Learn_forest.forest_animal_image()

        pygame.display.update()
        pygame.display.flip()
    
class Main:
    def __init__(self):
        pygame.init()
        self.running = True
           
    def run(self):   


        while self.running:
            self.intro = Text('Esi sveicināts lielajā meža spēlē!', (150, 50)).draw()
            memory_game_image = pygame.image.load("meza_dzivnieki/vilks.png").convert_alpha()
            learn_forest_image = pygame.image.load("meza_dzivnieki/lapsa.png").convert_alpha()
            self.memory_game_button = Button(200, 250, memory_game_image, 1).draw()
            self.learn_forest_button = Button(500, 250, learn_forest_image, 1).draw()          
          
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if self.memory_game_button:
                    Read_loud.say('Memory game')
                    Memory_game().run()
                if self.learn_forest_button:
                    Read_loud.say('Learn forest')
                    Crosshair_game().run()
                pygame.display.flip()
        pygame.quit()
    
if __name__ == '__main__':
    Main().run()
    
    
