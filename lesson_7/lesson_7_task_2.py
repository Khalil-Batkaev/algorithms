from random import uniform

"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке 
[0; 50). Выведите на экран исходный и отсортированный массивы
"""


def merge_sort(data):
    length = len(data)
    spam = []
    id_left = id_right = 0

    if length < 2:  # Базовый случай - массив из 1 элемента уже отсортирован
        return data

    new_length = length // 2
    left_data, right_data = merge_sort(data[:new_length]), merge_sort(data[new_length:])  # Приводим массив к базовому

    while id_left < len(left_data) and id_right < len(right_data):  # Сравниваем подмассивы пока есть хоть один из них
        # Добавляем во временный список меньшее значение, при этом двигаемся по списку, откуда забрали элемент
        if left_data[id_left] > right_data[id_right]:
            spam.append(right_data[id_right])
            id_right += 1
        else:
            spam.append(left_data[id_left])
            id_left += 1

    # Добавление оставшегося массива в конец временного
    spam += left_data[id_left:]
    spam += right_data[id_right:]

    return spam


MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10

array = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
eggs = merge_sort(array)
print(eggs)
