def headsort(lista):
    build_max_head(lista)
    for i in range(len(lista) - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        max_head(lista, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_head(lista):
    length = len(lista)
    start = parent(length - 1)
    while start >= 0:
        max_head(lista, index=start, size=length)
        start = start - 1


def max_head(lista, index, size):
    l = left(index)
    r = right(index)
    if (l < size and lista[l] > lista[index]):
        largest = l
    else:
        largest = index
    if (r < size and lista[r] > lista[largest]):
        largest = r
    if (largest != index):
        lista[largest], lista[index] = lista[index], lista[largest]
        max_head(lista, largest, size)


lista = input('Введите список чисел: ').split()
lista = [int(x) for x in lista]
headsort(lista)
print('Отсортированный список: ', end='')
print(lista)