from random import randint
from collections import Counter

"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, 
в другой — не больше медианы
"""

"""
Не знаю, будет зачтён такой способ решения или нет, но всё же )
Использовал встроенные модули и функции, поэтому и сомнения...

Асимптотическая сложность в худшем случае(все элементы массива уникальны) - квадратичная O(n^2), в лучшем 
случае(элементы, количество которых равно медиане, совпадают/равны) - линейная O(n). 
Соответственно, алгоритм будет эффективен только на массиве с повторяющимися элементами...

Ну и на всякий, если не будет зачтено первое решение, сделал через сортировку расчёской
"""


def search_median(data):
    qty_num = Counter(data)
    median = len(data) // 2 + 1
    qty = 0

    while qty < median:
        check_num = min(qty_num)
        qty += qty_num[check_num]
        del qty_num[check_num]

    return check_num


def brush_sort(data):
    length = len(data)
    step = length - 1

    while step:
        is_sorted = True

        for i in range(length - step):  # Проходимся по массиву каждый раз сужая шаг
            j = i + step

            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                is_sorted = False

        step = int(step / 1.247)  # Определяем шаг по выведенному числу

        if step == 1:
            if is_sorted:
                break


MIN_ITEM = 0
MAX_ITEM = 10

size = int(input('Введите целое число m: '))
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(size * 2 + 1)]
spam = array.copy()

print(f'Медиана массива - {search_median(array)}')
brush_sort(spam)
print(f'Медиана массива - {spam[size]}')

# for size in range(150):
#     array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(size * 2 + 1)]
#     spam = array.copy()
#     brush_sort(spam)
#     print(spam[size] == search_median(array))
