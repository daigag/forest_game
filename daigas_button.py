import pygame
from pygame.locals import *
import csv
import pandas as pd

pygame.init()


screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

font = pygame.font.SysFont('Constantia', 30)


#define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0

# with open ('learn_forest_data/input_data.csv', encoding="utf-8") as file:
#     reader = csv.reader(file, delimiter=',')
#     line_count = 0
#     for row in reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')



class button():
		
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

# def text_on_button():
#     with open ('learn_forest_data/input_data.csv', encoding="utf-8") as file:
#         reader = csv.reader(file, delimiter=',')
#         line_count = 0
#         for row in reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'You see the {row[3]}, in latvian - {row[2]}.')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')
#     return {row[3]}



def text_on_button():
    with open ('learn_forest_data/input_data.csv', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0
        if line_count == 0:
            for row in reader:
                line_count += 1
            #print(f'You see the {row[3]}, in latvian - {row[2]}.')
            print(f'{row[3]}')
                #line_count += 1
        #print(f'Processed {line_count} lines.')
        
text = text_on_button()

again = button(75, 200, print(text))
quit = button(325, 200, 'Quit?')
down = button(75, 350, 'Down')
up = button(325, 350, 'Up')


run = True
while run:

	screen.fill(bg)

	if again.draw_button():
		print('Again')
		counter = 0
	if quit.draw_button():
		print('Quit')
	if up.draw_button():
		print('Up')
		counter += 1
	if down.draw_button():
		print('Down')
		counter -= 1

	counter_img = font.render(str(counter), True, red)
	screen.blit(counter_img, (280, 450))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False	


	pygame.display.update()


pygame.quit()