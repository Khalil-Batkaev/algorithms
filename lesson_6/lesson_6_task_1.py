from random import randint
from operator import itemgetter
from sys import getsizeof
from timeit import timeit

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

"""
Для решения данного задания мною была выбрана задача lesson_3_task_6:
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать

Тесты проводились на массиве, состоящим из 10 000 элементов
Версия интерпретатора Python - 3.9.6
Версия и разрядность ОС - Win10 Home 64-bit

Были написаны 3 варианта решения данной задачи:
1. Решение, которое было изначальным
2. Решение через встроенные функции
3. Решение для теста с модулем operator

Обекты 1-го решения:
Объект array = [23, 100, 69, 54, 86, 54, 64, 67, 36, 59] относится к <class 'list'> и размер равен 364 764
Объект max_number = 100 относится к <class 'int'> и размер равен 28
Объект min_number = 0 относится к <class 'int'> и размер равен 24
Объект max_id = 18 относится к <class 'int'> и размер равен 28
Объект min_id = 1 относится к <class 'int'> и размер равен 28
Объект sum_number = 1099 относится к <class 'int'> и размер равен 28
Объект i = 17 относится к <class 'int'> и размер равен 28
Объект num = 83 относится к <class 'int'> и размер равен 28
Всего объектов и их общий размер для 1-го решения: 8 - 364 956
------
Обекты 2-го решения:
Объект array = [23, 100, 69, 54, 86, 54, 64, 67, 36, 59] относится к <class 'list'> и размер равен 364 764
Объект id_min = 1 относится к <class 'int'> и размер равен 28
Объект id_max = 18 относится к <class 'int'> и размер равен 28
Объект sum_number = 1099 относится к <class 'int'> и размер равен 28
Всего объектов и их общий размер для 2-го решения: 4 - 364 848
------
Обекты 3-го решения:
Объект array = [23, 100, 69, 54, 86, 54, 64, 67, 36, 59] относится к <class 'list'> и размер равен 364 764
Объект spam = [(0, 23), (1, 100), (2, 69), (3, 54), (4, 86), (5, 54), (6, 64), (7, 67), (8, 36), (9, 59)] относится 
к <class 'list'> и размер равен 1 204 760
Объект id_min = 1 относится к <class 'int'> и размер равен 28
Объект id_max = 18 относится к <class 'int'> и размер равен 28
Объект sum_number = 1099 относится к <class 'int'> и размер равен 28
Всего объектов и их общий размер для 3-го решения: 5 - 1 569 608

Также, проверил время выполнения решений, чтобы оценить и ещё и с данной стороны. 
Сложность у всех алгоритмов линейная O(n).

first_solve -> 9.3070033
second_solve -> 2.391946000000001
third_solve -> 35.7749175

Исходя из полученных данных, самым незатратным по памяти стало решение 2: все переменные в количестве 4 заняли 364 848 
байт, при этом входящий анализируемый список имеет размер 364 764 байта, а переменные, используемые для расчетов 
всего 84 байта. Размер данных переменных никак не зависит от размера входящего списка, только от объектов, входящих 
в список.
Это же решение оказалось и самым быстрым ~2.39 секунды, несмотря на то, что происходит 4 итерации по списку - больше, 
чем во всех других вариантах решения.

На втором месте - первое решение: объём памяти - 364 956 байт, из которых используемые для алгоритма переменные в 
количестве 8 штук заняли 192 байта. Также как и во втором решении - их размер зависит только от входящих в список 
объектов, а не от длины списка.
Эффективность по времени также оказалась на втором месте: ~9.30 секунд и при этом всего 2 итерации 
по списку - минимальное количество.

Ну и на последнем месте закономерно оказалось 3 решение: 1 569 608 байт, при этом используемые переменные в количестве 
5 заняли 1 204 844 байта и их размер будет расти пропорционально увеличению входного списка.
Эффективность по времени также хуже всех - ~35.77 секунд и 3 итерации по списку.
"""


def first_solve(array):
    max_number, min_number = float('-inf'), float('inf')
    max_id, min_id = -1, -1
    sum_number = 0

    for i, num in enumerate(array):
        if num > max_number:
            max_number = num
            max_id = i
        if num < min_number:
            min_number = num
            min_id = i

    if min_id > max_id:
        min_id, max_id = max_id, min_id
    for i in range(min_id + 1, max_id):
        sum_number += array[i]

    if __name__ == '__main__':
        all_objects.append(locals())

    return f'Сумма элементов между минимальным и максимальным значениями равна: {sum_number}'


def second_solve(array):
    id_min = array.index(min(array))
    id_max = array.index(max(array))

    if id_min > id_max:
        id_min, id_max = id_max, id_min

    sum_number = sum(array[id_min + 1: id_max])

    if __name__ == '__main__':
        all_objects.append(locals())

    return f'Сумма элементов между минимальным и максимальным значениями равна: {sum_number}'


def third_solve(array):
    spam = list(enumerate(array))
    id_min = min(spam, key=itemgetter(1))[0]
    id_max = max(spam, key=itemgetter(1))[0]

    if id_min > id_max:
        id_min, id_max = id_max, id_min

    sum_number = sum(array[id_min + 1: id_max])

    if __name__ == '__main__':
        all_objects.append(locals())

    return f'Сумма элементов между минимальным и максимальным значениями равна: {sum_number}'


# Рекурсивное решение тоже есть, но оно упирается в свой потолок на массиве из 994 элемента
# Переложил решение на циклы под задачу и данные, не универсальное...
def get_size(data):
    data_size = getsizeof(data)

    if not hasattr(data, '__iter__') or isinstance(data, str):
        return data_size

    for object in data:
        if not hasattr(object, '__iter__') or isinstance(object, str):
            data_size += getsizeof(object)
        else:
            data_size += getsizeof(object)
            for item in object:
                data_size += getsizeof(item)
    return data_size


def get_size_rec(data, is_first=True):
    data_size = getsizeof(data) if is_first else 0

    if not hasattr(data, '__iter__') or isinstance(data, str):
        return getsizeof(data)

    if not len(data):
        return 0

    if hasattr(data[0], '__iter___') and not isinstance(data, str):
        res = get_size_rec(data[0], is_first=True) + get_size_rec(data[1:], is_first=False)

    else:
        res = get_size_rec(data[0]) + get_size_rec(data[1:], is_first=False)

    return res + data_size


SIZE = 994
MIN_ITEM = 0
MAX_ITEM = 100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

all_objects = []

# print('first_solve', timeit('first_solve(array)', globals=globals(), number=10_000), sep=' -> ')
# print('second_solve', timeit('second_solve(array)', globals=globals(), number=10_000), sep=' -> ')
# print('third_solve', timeit('third_solve(array)', globals=globals(), number=10_000), sep=' -> ')

print(first_solve(array))
print(second_solve(array))
print(third_solve(array))

for i, objects in enumerate(all_objects):
    total_size = 0
    count = 0
    print('------')
    print(f'Обекты {i + 1}-го решения:')
    for name, object in objects.items():
        size = get_size(object)
        total_size += size
        count += 1
        print(
            f'Объект {name} = {object[:10] if hasattr(object, "__iter__") else object} относится к {type(object)} '
            f'и размер равен {size}')

    print(f'Всего объектов и их общий размер для {i + 1}-го решения: {count} - {total_size}')

print('И рекурсивное решение')

for i, objects in enumerate(all_objects):
    total_size = 0
    count = 0
    print('------')
    print(f'Обекты {i + 1}-го решения:')
    for name, object in objects.items():
        size = get_size_rec(object)
        total_size += size
        count += 1
        print(
            f'Объект {name} = {object[:10] if hasattr(object, "__iter__") else object} относится к {type(object)} '
            f'и размер равен {size}')

    print(f'Всего объектов и их общий размер для {i + 1}-го решения: {count} - {total_size}')
