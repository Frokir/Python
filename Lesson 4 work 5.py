import functools


def multiplier(a, b):
    return a * b


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)

print(functools.reduce(multiplier, my_list))
