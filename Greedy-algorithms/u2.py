'''A thief sneaks into a museum and wants to steal N exhibits. Each exhibit has its own weight and price. 
The thief can make M visits, each time taking away K kg of weight. Determine what the thief has to take to 
maximize the amount stolen.'''
import random

n = int(input('Введите сколько экспонатов вор хочет украсть: '))
m = int(input('Введите количество заходов, которое хочет сделать вор: '))
k = int(input('Введите количество килограммов, которое вор может унести за один заход: '))

#things = [(3000, 30), (2000, 20), (1500, 15)]  #Пример набора, на котором жадный работает неправильно(

things = []
for i in range(n):     # Создаем список с товарами
    cost = random.randint(100, 3000)   # Присваиваем им рандомные стоимость и вес
    weight = random.randint(1, 100)
    things.append((cost, weight))

print('Стоимости и массы экспонатов, находящихся в музее: ', things)

things.sort(key=lambda x:x[0])
things.reverse()    # Упорядочиваем  товары по убыванию стоимости
stolen_things = []   # Создаем список украденых
for i in range(m):   # Делаем несколько заходов в наш музей
    cur_k = k
    j = 0
    while j < len(things):
        if cur_k < things[j][1]:    # Берем вещь с наибольшей стоимостью, которую еще можем унести
            j += 1
            continue

        else:
            cur_k -= things[j][1]  # Берем вещь с наибольшей стоимостью, которую еще можем унести
            stolen_things.append(things.pop(j))  # Убираем из списка украденную вещь и добавляем в список украденного
print('Стоимости и масса экспонатов, которые вор смог украсть: ', stolen_things)