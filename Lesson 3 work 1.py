def divider(a, b):
    if b != 0:
        answear = a / b
    else:
        answear = 'Error'
    return answear


if __name__ == '__main__':
    print(divider(1, 4))
    input('Enter for exit')
