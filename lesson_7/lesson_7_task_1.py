from random import randint

"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке 
[-100; 100). Выведите на экран исходный и отсортированный массивы.
"""


def bubble_sort(data, is_reverse=True):  # Флаг про разворот добавил для себя на будущее
    n = len(data) - 1

    for _ in range(n):
        is_sorted = True  # Добавил проверку на уже отсортированный список

        for i in range(n):
            j = i + 1
            # Выталкиваем минимальный/максимальный элемент в конец массива
            if data[i] < data[j] if is_reverse else data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                is_sorted = False  # Если не было перестановок, то уже отсортирован

        if is_sorted:
            break


MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
bubble_sort(array)
print(array)
