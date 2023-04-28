cities = ['Москва', 'Уфа', 'Санкт-Петербург', 'Рязань', 'Екатеринбург']
print('Задача: сосчитать количество различных вариантов сочетаний')
combinations = []
for a1 in range(len(cities)):
    for a2 in range(1, len(cities)):
        for a3 in range(2, len(cities)):
            for a4 in range(3, len(cities)):
                for a5 in range(4, len(cities)):
                    comb = [a1, a2, a3, a4, a5]  # перебираем n! сочетаний и добавляем в список
                    combinations.append([a1, a2, a3, a4, a5])
print(len(combinations))


