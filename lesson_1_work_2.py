second = input("Enter second: ")

hour = int(second) // 3600
minute = (int(second) % 3600) // 60
seconds = (int(second) % 3600) % 60

print(f'{hour}:{minute}:{seconds}')