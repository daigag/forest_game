import csv


class Open_csv:

    def open_file():
        with open('learn_forest_data/input_data.csv', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=',')
            line_count = 0
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
