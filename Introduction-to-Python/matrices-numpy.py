import numpy as np
from numpy import linalg as ko
matrix_1 = np.array(range(6), int).reshape((2, 3))
matrix_2 = np.array(range(6),int).reshape((3,2))
matrix_trans = matrix_1.transpose()
print('Матрица:',matrix_1)
print('Вторая матрица:',matrix_2)
print('Транспонирование матрицы:',matrix_trans)
print('Умножение матриц:',np.matmul(matrix_1,matrix_2))
print('Ранг матрицы:',ko.matrix_rank(matrix_1))