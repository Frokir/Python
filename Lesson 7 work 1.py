class Matrix:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        answear = ''
        for line in self.list_of_list:
            for el in line:
                answear += str(el) + ' '
            answear += '\n'
        return answear

    def summator(self, x_list, y_list):
        answear_list = []
        for x, y in zip(x_list, y_list):
            answear_list.append(x + y)
        return answear_list

    def __add__(self, other):
        my_list = []
        for first_obj_list, second_obj_list in zip(self.list_of_list, other.list_of_list):
            my_list.append(self.summator(first_obj_list, second_obj_list))
        return Matrix(my_list)


matrix = Matrix([[10, 20, 30], [11, 21, 31], [12, 22, 32]])
matrix_2 = Matrix([[20, 30, 40], [21, 31, 41], [22, 32, 42]])
print(matrix)
print(matrix_2)
matrix_3 = matrix + matrix_2
print(matrix_3)
