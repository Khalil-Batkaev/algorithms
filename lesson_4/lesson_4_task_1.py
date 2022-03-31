import random
import collections
import timeit
import cProfile

"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех
уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
Для анализа был выбран lesson_3_task_4 Определить, какое число в массиве встречается чаще всего

Были написаны 3 варианта решения данной задачи:
1. Решение через словарь, которое было изначальным - dict_solve
2. Решение через список - list_solve
3. Решение с помощью встроенного модуля collections и объекта Counter - counter_solve

---- dict_solve
dict_solve -> 1000 -> 0.9051179
dict_solve -> 2000 -> 1.4874038
dict_solve -> 4000 -> 2.9676365
dict_solve -> 8000 -> 5.3817031
dict_solve -> 16000 -> 10.1855375
dict_solve -> 32000 -> 19.8301837
dict_solve -> 64000 -> 41.5543411
dict_solve -> 128000 -> 92.5086859
dict_solve -> 256000 -> 185.54048200000003
dict_solve -> 512000 -> 373.55512279999994
dict_solve -> 1024000 -> 744.9644635000001

5 function calls in 0.147 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.147    0.147 <string>:1(<module>)
        1    0.147    0.147    0.147    0.147 lesson_4_task_1.py:86(dict_solve)
        1    0.000    0.000    0.147    0.147 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

---- list_solve (для timeit количество повторений было уменьшено в 100 раз, а для cProfile длина массива - в 10 раз)
list_solve -> 1000 -> 0.7864007
list_solve -> 2000 -> 2.7415855
list_solve -> 4000 -> 11.161239
list_solve -> 8000 -> 47.6643855
list_solve -> 16000 -> 217.57944310000002
list_solve -> 32000 -> 838.5380522

5 function calls in 283.263 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  283.263  283.263 <string>:1(<module>)
        1  283.263  283.263  283.263  283.263 lesson_4_task_1.py:106(list_solve)
        1    0.000    0.000  283.263  283.263 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

---- counter_solve
counter_solve -> 1000 -> 0.3090367999998307
counter_solve -> 2000 -> 0.5034571999999571
counter_solve -> 4000 -> 0.9063851000000795
counter_solve -> 8000 -> 1.6823971000001166
counter_solve -> 16000 -> 3.277260800000022
counter_solve -> 32000 -> 6.208246800000097
counter_solve -> 64000 -> 13.18142940000007
counter_solve -> 128000 -> 29.70828090000009
counter_solve -> 256000 -> 62.9974443000001
counter_solve -> 512000 -> 128.7095941
counter_solve -> 1024000 -> 260.7679293000001

30 function calls (22 primitive calls) in 0.054 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.053    0.053 <string>:1(<module>)
        1    0.000    0.000    0.053    0.053 __init__.py:581(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:600(most_common)
        1    0.000    0.000    0.053    0.053 __init__.py:649(update)
        5    0.000    0.000    0.000    0.000 _collections_abc.py:409(__subclasshook__)
        1    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
      5/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
        1    0.000    0.000    0.053    0.053 lesson_4_task_1.py:104(counter_solve)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      5/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.053    0.053    0.053    0.053 {built-in method _collections._count_elements}
        1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

Исходя из полученных данных, сложность алгоритмов сложилась следующая:
- самым эффективным и быстрым стало решение через встроенный модуль collections и объект Counter. Сложность данного 
алгоритма линейная О(n), соответственно время выполнения растёт пропорционально с увеличением n
- вторым по эффективности и скорости выполнения стало решение с помощью словаря. Сложность тоже линейная О(n), но
время выполнения выше, из-за меньшей оптимизации...
- и худшим вариантом стал алгоритм с использованием списка. Сложность квадратичная О(n²), соответственно время 
выполнения растёт квадратично с увеличением n

Следовательно, использовать стоит алгоритм, использующий встроенный модуль collections и объект Counter. 
При одинаковой сложности, он в 2,5-3 раза быстрее алгоритма со словарём, а про решение с помощью списка забыть навсегда.
"""


# 1. Решение, которое уже было
def dict_solve(numbers_list):
    result_dict = {}
    max_value = 1
    max_number = None

    for num in numbers_list:
        if num not in result_dict:
            result_dict[num] = 1
        else:
            result_dict[num] += 1

    for key, val in result_dict.items():
        if result_dict[key] > max_value:
            max_value = val
            max_number = key

    return f'Чаще всего встречается число: {max_number}, повторений {max_value}'


# 2. Решение через список
def list_solve(numbers_list):
    max_value = 1
    end = len(numbers_list)
    max_number = None

    for i, check_num in enumerate(numbers_list):
        count = 1

        for j in range(i + 1, end):
            if check_num == numbers_list[j]:
                count += 1

        if count > max_value:
            max_value = count
            max_number = check_num

    return f'Чаще всего встречается число: {max_number}, повторений {max_value}'


# 3. Решение с помощью встроеной модуля collections.Counter
def counter_solve(numbers_list):
    result = collections.Counter(numbers_list)
    max_number, max_value = result.most_common(1)[0]

    return f'Чаще всего встречается число: {max_number}, повторений {max_value}'


MIN_ITEM = 0
MAX_ITEM = 100
size = 500

while size <= 512000:
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    size *= 2

    print('dict_solve', size, timeit.timeit('dict_solve(array)', globals=globals(), number=10000), sep=' -> ')
    print('counter_solve', size, timeit.timeit('counter_solve(array)', globals=globals(), number=10000), sep=' -> ')
    print('list_solve', size, timeit.timeit('list_solve(array)', globals=globals(), number=100), sep=' -> ')

size = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

cProfile.run('dict_solve(array)')
cProfile.run('counter_solve(array)')

size = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

cProfile.run('list_solve(array)')
