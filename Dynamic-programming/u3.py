'''An array N is given, consisting of n random integers in the range 
in the range -100 to 100. Find the largest continuous 
increasing sequence of numbers inside the array (the length 
series for which N[i]<N[i+1]<N[i+2]<...<N[i+m] is true, where i≥0 and 
i+m≤n-1).'''
from random import randint

def podposl(a: list):
    counter = [1] * len(a) #Создаем список, в котором будем хранить количество подряд идущих возрастающих элементов
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            counter[i] = counter[i-1] + 1   #Смотрим, какова длина возрастающей цепочки на пред. элементе и увеличиваем на 1

    i = counter.index(max(counter)) #Находим индекс последнего элемента в самой длинной цепочке
    max_len = counter[i]
    return a[i - max_len + 1: i + 1]

n = int(input('Введите длину массива: '))
N = []
for i in range(n):    #Рандомно создаем список
    a = randint(-100,100)
    N.append(a)

print('Наибольшая возрастающая подпоследовательность:')
print(podposl(N))