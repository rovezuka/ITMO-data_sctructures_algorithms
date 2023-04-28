'''The user needs to give change of N rubles. 
He has M1 coins of face value S1, M2 coins of face value S2, M3 coins of face value S3 and M4 coins of face 
value S4. It is necessary to find the smallest combination of the given coins, which will allow to get a 
total of N.'''
n = int(input('Введите сумму: '))
m1, s1 = map(int, input('Введите количество монет и первый номинал: ').split())
m2, s2 = map(int, input('Введите количество монет и второй номинал: ').split())
m3, s3 = map(int, input('Введите количество монет и третий номинал: ').split())
m4, s4 = map(int, input('Введите количество монет и четвертый номинал: ').split())
values = [(s1, m1), (s2, m2), (s3, m3), (s4, m4)]   #Создаем список, содержащий пары (номинал, кол-во)
values.sort(key=lambda x:x[0])
values.reverse()    #Сортируем от большего номинала к меньшему
change = [] #Список с нашей сдачей
for i in range(4):  #Проходимся по списку и сначала берем монеты наибольшего номинала
    coins = min(n // values[i][0], values[i][1])    #Берем наименьшее из кол-ва монет номинала и
                                                        # кол-вом монет, которые можем взять
    change.append((values[i][0], coins))    #Добавляем сдачу в список
    n -= coins * values[i][0]   #Вычитаем сумму, которую набрали из изначальной

if n == 0:
    for money in change:
        print(f'Нужно взять {money[1]} монет номинала {money[0]}')
else:
    print('Жадный алгоритм думает, что сдачу не удастся сдать')