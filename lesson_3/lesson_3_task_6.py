import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать
"""

max_number, min_number = 0, 100
max_id, min_id = -1, -1
sum_number = 0
total = 0

for i, num in enumerate(array):
    # Решил использовать для расчёта первое вхождение в массив минимального и максимального элементов
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

print(f'Сумма элементов между минимальным и максимальным значениями равна: {sum_number}')
