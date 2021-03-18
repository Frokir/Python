with open('text1.txt') as my_file:
    text_list = my_file.readlines()
    print('Колличество строк: ', len(text_list))
    number_of_line = 1
    for line in text_list:
        print(f'В {number_of_line} строке, {len(line.split())} слов(а).')
        number_of_line += 1
