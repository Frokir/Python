def main():
    summa = 0
    flag = 1
    while flag:
        string = input('Введите строку: ')
        string = string.split(' ')
        for i in string:
            try:
                i = int(i)
                summa += i
            except:
                print(summa)
                flag = 0
                break

        if flag:
            print(summa)


if __name__ == '__main__':
    main()
