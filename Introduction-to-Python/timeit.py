import timeit
import numpy
from numpy.linalg import inv


def matrix_create():  # функция создания матрицы
    a, b = 3, 3
    matrix = []
    for x in range(a):  # количество строк
        m = []
        for y in range(b):  # количество столбцов
            m.append(int(input(f'Введите значение для ячейки [{x}][{y}]: ')))  # пользователь заполняет каждую ячейку
        matrix.append(m)
    return matrix


matrix = matrix_create()  # создание матрицы
matrix_numpy = matrix

def determinant(matrix):
    det_a = matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]\
    +matrix[1][0]*matrix[2][1]*matrix[0][2] - matrix[0][2]*matrix[1][1]*matrix[2][0]-matrix[0][1]*matrix[1][0]\
            *matrix[2][2]-matrix[0][0]*matrix[1][2]*matrix[2][1]
    return det_a


det = determinant(matrix)  # нахожу детерминант

def minor(matrix, x, y):
    res = []
    for a in range(3):
        m = []
        for b in range(3):
            if a != x and b != y:
                m.append(matrix[a][b])
        if m != []:
            res.append(m)
    return res[0][0]*res[1][1] - res[0][1]*res[1][0]


def algebraic_additions(matrix):
    res = []
    for x in range(3):
        m = []
        for y in range(3):
            m.append(((-1)**(x+y))*minor(matrix, x, y))  # нахожу алг дополнение к каждому элементу
        res.append(m)
    return res


def matrix_transposition_det(matrix):  # транспонирование матриц + делим на детерминант
    global det
    res = []
    for i in range(len(matrix[0])):
        m = []
        for x in range(len(matrix)):
            m.append(matrix[x][i]//det)
        res.append(m)
    return res


matrix = algebraic_additions(matrix)  # матрица алг дополнений
matrix = matrix_transposition_det(matrix) # транспонирую
print(matrix)

# сравнение быстродействия
start_time = timeit.default_timer()
matrix_transposition_det(algebraic_additions(matrix))  # моя функция
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
inv(numpy.array([matrix_numpy]))  # обратная матрица через numpy
print(timeit.default_timer() - start_time)