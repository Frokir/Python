number = input('Enter number: ')
max = '0'
while number:
    if max <= number[-1]:
        max = number[-1]
    # if len(number) > 1:
    number = number[:-1]
    # else:
    #     break
print(max)