import timeit
from scratch_5 import sort
from scratch_5 import comb_sort

numbers = int(input('Введите "1", если хотите выбрать быструю сортировку и "2", если хотите выбрать сортировку расческой: '))
sequince = [5, 0, -2, 7, 3]
if numbers == 1:
    print(sort([1,3,2,7,1,6]))
elif numbers == 2:
    comb_sort(sequince)
    print(sequince)
else:
    print('Введите правильное число')

start_time = timeit.default_timer()
sort([1,3,2,7,1,6])  # быстрая сортировка
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
comb_sort(sequince)  # сортировка расческой
print(timeit.default_timer() - start_time)