print('Введите число которое вы загадали: ')
element = int(input())
array = [1,2,3,4,5,6,7]
array.sort()
count = 0
print('Ищем число ' + str(element))
def binary_search(array, element, start, end):
    global count
    if start > end:
        return -1
    count +=1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)
print('Индекс числа '+ str(element)   + ' в массиве равняется ' + str(binary_search(array,element,0,len(array))))
print('Количество шагов: ', count)

