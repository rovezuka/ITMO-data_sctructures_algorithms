from random import randint

x, y, z = map(int, input().split())  # Ввод трех чисел x, y и z с клавиатуры и присваивание их переменным

matrix = []  # Создание пустого списка matrix

# Цикл для заполнения списка matrix случайными числами
for i in range(x):
    a1 = []
    for j in range(y):
        a2 = []
        for k in range(z):
            a3 = randint(1, 10)  # Генерация случайного числа от 1 до 10
            a2.append(a3)
        a1.append(a2)
    matrix.append(a1)
print(matrix)  # Вывод списка matrix

i = 0
j = 0
k = 0
s = 0
print(matrix[i][j][k])  # Вывод значения элемента matrix[i][j][k]

visited = []  # Создание пустого списка visited
visited.append((0, 0, 0))  # Добавление кортежа (0, 0, 0) в список visited

# Цикл while для перемещения по матрице и суммирования значений элементов
while (i != x - 1 or j != y - 1 or k != z - 1):
    neighbours = []  # Создание пустого списка neighbours
    
    # Поиск соседей текущей позиции (i, j, k) и добавление их в список neighbours
    if k < z - 1:
        neighbours.append((matrix[i][j][k + 1], (i, j, k + 1)))
    if k > 0:
        neighbours.append((matrix[i][j][k - 1], (i, j, k - 1)))
    if j < y - 1:
        neighbours.append((matrix[i][j + 1][k], (i, j + 1, k)))
    if j > 0:
        neighbours.append((matrix[i][j - 1][k], (i, j - 1, k)))
    if i < x - 1:
        neighbours.append((matrix[i + 1][j][k], (i + 1, j, k)))
    if i > 0:
        neighbours.append((matrix[i - 1][j][k], (i - 1, j, k)))
    
    neighbours.sort(key=lambda x: x[0])  # Сортировка соседей по значению первого элемента
    
    for n in neighbours:
        if n[1] not in visited:
            visited.append(n[1])  # Добавление позиции соседа в список visited
            s += n[0]  # Добавление значения соседа к сумме s
            i, j, k = n[1]  # Обновление текущей позиции (i, j, k) до позиции соседа
            break

print(s)  # Вывод суммы значений элементов матрицы
