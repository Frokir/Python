def int_func(word):
    word = word.capitalize()
    return word


def main():
    string = input('Введите строку: ')
    splited_string = string.split()
    new_string = ''
    for word in splited_string:
        new_string += int_func(word) + ' '

    print(new_string)


if __name__ == '__main__':
    main()
