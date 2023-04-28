print('Задача: отсортировать список по возрастанию')


def quicksort(array):
    if len(array) < 2:
        return array  # базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    else:
        pivot = array[len(array) // 2]  # рекурсивный случай, берем средний элемент
        less = [i for i in array[:] if i <= pivot and array.index(i) != array.index(pivot)]  # подмассивы всех элементов, меньших опорного
        greater = [i for i in array[:] if i > pivot and array.index(i) != array.index(pivot)]  # подмассивы всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3, 111, 12312, 44, 0, -1, -100]))