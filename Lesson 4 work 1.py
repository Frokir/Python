from sys import argv


def wage():
    name, hour, cost, premium = argv
    return (int(hour) * int(cost)) + int(premium)


if __name__ == '__main__':
    print(wage())
    input('Enter for exit')
