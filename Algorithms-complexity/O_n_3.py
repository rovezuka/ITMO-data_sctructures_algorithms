print('Задача: вывести различные сочетания длиной три из элементов списка')
numbers = [1, 2, 3, 4, 5]
for a in numbers:
    for b in numbers:
        for c in numbers:
            print(a, b, c)