print('Задача: сложить индексы максимального, минимального и среднего числа списка')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr, item):
    global step
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high -= 1
        else:
            low +=1
    return None
print(binary_search(numbers, 5) + binary_search(numbers, 1) + binary_search(numbers, 10))