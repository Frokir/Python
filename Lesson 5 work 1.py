with open('text_0.txt', 'w') as my_file:
    while True:
        text = input()
        if text:
            my_file.write(text + '\n')
        else:
            break
