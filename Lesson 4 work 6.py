from itertools import count, cycle


def my_count(x, stop=10):
    meter = 0
    answear = []
    for i in count(x):
        answear.append(i)
        meter += 1
        if meter == stop:
            return answear
            break


def my_cycle(my_list, stop=5):
    meter = 0
    answear = []
    for i in cycle(my_list):
        answear.append(i)
        meter += 1
        if meter == stop:
            return answear
            break


print(my_count(15))
print(my_count(15, 5))

print(my_cycle('123'))
print(my_cycle(['123', 246, '111'], 15))
