#Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#Пример:
#[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
#[1, 5, 2, 3, 4, 1, 7] => [1, 5]

list1 = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = [1, 5, 2, 3, 4, 1, 7]

def InAscendingOrder(array):
    print(f'Исходный список {array}')
    array.sort()
    res = [array[0], array[0]]
    for i in range(1, len(array)):
        if array[i]-array[i-1] == 1 or array[i]-array[i-1] == 0:
            last = array[i]
        else:
            break
        res[1] = last
    return res

print(f'Возрастающая последовательность по первому и второму списку от/до: {InAscendingOrder(list1)};{InAscendingOrder(list2)}')