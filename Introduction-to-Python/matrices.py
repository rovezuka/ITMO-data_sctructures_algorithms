import copy
from itertools import combinations
count_matrix=0
def create_Matrix(count_matrix): #функция ввода новой матрицы
    print('Введите количество строк вашей матрицы:')
    i = int(input())
    print('Введите количество столбцов вашей матрицы:')
    j = int(input())
    Matrix_m=[0]*i
    for n in range(i):
        Matrix_m[n]=[0]*j
    print('Поочередно вводите элементы вашей матрицы:')
    for count_i in range(i):
        for count_j in range(j):
            print(f'Введите элемент [{count_i+1}][{count_j+1}]')
            new_element=int(input())
            Matrix_m[count_i][count_j]=new_element
    count_matrix+=1
    return Matrix_m

Matrix_all=[] #список, содержащий все введенные матрицы
Matrix_all.append(create_Matrix(count_matrix)) #вводим первую матрицу
print('Выберите действие:', '\n', '1 - Транспонирование матрицы', '\n', '2 - Умножение матриц', '\n', '3 - Определение ранга матрицы')
number_action = int(input())
if number_action==1:
    def Matrix_transposition(Matrix):  # транспонирование матриц
        res = []
        for j in range(len(Matrix[0])):
            m = []
            for i in range(len(Matrix)):
                m.append(Matrix[i][j])
            res.append(m)
        return res
    print(Matrix_transposition(Matrix_all[0]))

if number_action==2:
    Matrix_all.append(create_Matrix(count_matrix)) #вводим вторую матрицу
    def Matrix_multiplication(Matrix_a, Matrix_b):  # умножение матриц
        sum = 0
        T_vr = []
        Matrix_c = []
        i_a = len(Matrix_a)
        j_a = len(Matrix_a[0])
        i_b = len(Matrix_b)
        j_b = len(Matrix_b[0])
        if j_a != i_b:
            return 'Операция умножения двух матриц выполнима только в том случае, если число столбцов в первом сомножителе равно числу строк во втором.'
        else:
            for q in range(i_a):
                for w in range(j_b):
                    for e in range(j_a):
                        sum += Matrix_a[q][e] * Matrix_b[e][w]
                    T_vr.append(sum)
                    sum = 0
                Matrix_c.append(T_vr)
                T_vr = []
            return (Matrix_c)
    print(Matrix_multiplication(Matrix_all[0],Matrix_all[1]))

if number_action==3:
    M_Matrix = []
    for i in range(len(Matrix_all[0])):
        for j in range(len(Matrix_all[0])):
            M_Matrix.append([i, j])

    def opred(M):
        if len(M) == len(M[0]) == 1:
            return M[0][0]
        else:
            sum = 0
            for j in range(len(M[0])):
                Matrix_vr = copy.deepcopy(M)
                for count_i in range(len(Matrix_vr)):
                    Matrix_vr[count_i].pop(j)
                Matrix_vr.pop(0)
                sum += M[0][j] * ((-1) ** (j + 2)) * (opred(Matrix_vr))
            return sum

    def check_minors(x):
        minors = list(combinations(M_Matrix, x ** 2))
        for minor in minors:
            minor_1 = []
            for k in range(len(minor)):
                minor_1.append(minor[k])
            minor_values = []
            MK = []
            for g in range(x ** 2):
                MK.append(Matrix_all[0][minor_1[g][0]][minor_1[g][1]])
                if len(MK) == x:
                    minor_values.append(MK)
                    MK = []
            Dict_i = {}
            Dict_j = {}
            for count_element in range(x ** 2):
                if minor_1[count_element][0] not in Dict_i:
                    Dict_i[minor_1[count_element][0]] = 1
                else:
                    Dict_i[minor_1[count_element][0]] += 1
                if minor_1[count_element][1] not in Dict_j:
                    Dict_j[minor_1[count_element][1]] = 1
                else:
                    Dict_j[minor_1[count_element][1]] += 1
            if len(Dict_i) == len(Dict_j) == x and opred(minor_values) != 0:
                return 1
        else:
            return 0

    k = 0
    for count_order in range(1, min(len(Matrix_all[0]), len(Matrix_all[0][0])) + 1):
        if check_minors(count_order) == 1:
            k = count_order
        else:
            break
    print(k)











