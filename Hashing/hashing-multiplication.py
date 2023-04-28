from random import uniform
#функция, которая превращает строковый ключ в число с помощью функции ord
def str_to_int(str):
    s = 0
    for i in range(len(str)):
        s += ord(str[i])
    return s
#функция хэширования, которая создает словарь типа ключ: индекс
def hash(M,mas,C):
    h = {}
    for i in mas:
        #если передали целое число, то оставляем его
        #если передали строку, то преобразуем ее в число
        if i.isdigit():
            K = int(i)
        else:
            K = str_to_int(i)
        #индекс элемента в хэш-таблице вычисляем по выражению M*((K*C)mod1)
        index = int(M*((K*C)%1))
        #добавляем в словарь
        h[i] = index
    return h
M = int(input('Введите длину массива\n'))
mas = input('Введите ключ(и) через пробел\n').split()
#генерируется рандомное C в интервале от 0 до 1
C = uniform(0,1)
print('C:',C)
print('Значения хэш-функции для введенных ключей:')
#вызывает функцию хэширования, передавая туда длину массива, ключи и C
h = hash(M,mas,C)
#выводим значение хэш-функции для каждого ключа
for a in h:
    print('h(',a,') = ',h[a],sep='')