print('Задача: умножить каждый элемент списка на среднее арифметическое всего списка')
numbers, len_list, sum_list = [1, 2, 3, 4, 5], 0, 0
for a in numbers: len_list += 1
for b in numbers: sum_list += b
for c in range(len_list): numbers[c] *= (sum_list/len_list)
print(numbers)
