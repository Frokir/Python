def my_func_1(a, b, c):  # Вариант 1
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return my_list[0] + my_list[1]


def my_func_2(*a):  # Вариант 2 принимает любое количесвто символов и суммирует два самых больших.
    my_list = sorted(a)
    return my_list[-1] + my_list[-2]


if __name__ == '__main__':
    print(my_func_1(4, 5, 8))
    print(my_func_2(4, 5, 8, 10))
    input('Enter for exit')
