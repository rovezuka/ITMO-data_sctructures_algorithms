def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return array

def comb_sort(sequince):
    step = int(len(sequince)/1.247)
    swap = 1
    while True:
        swap = 0
        i = 0
        while i + step < len(sequince):
            if sequince[i] > sequince[i+step]:
                sequince[i], sequince[i+step] = sequince[i+step], sequince[i]
                swap += 1
            i = i + 1
        if (step == 1 and swap == 0):
            break
        step = int(step/1.247)
        if step < 1:
            step = 1