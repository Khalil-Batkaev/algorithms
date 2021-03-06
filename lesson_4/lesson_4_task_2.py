import timeit
import cProfile
import math

"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту
"""

"""
---- prime
prime -> 50 -> 0.13525610000000002
prime -> 100 -> 0.2350503
prime -> 200 -> 0.48822450000000006
prime -> 400 -> 1.1794740000000001
prime -> 800 -> 2.9422362
prime -> 1600 -> 7.4737522
prime -> 3200 -> 18.298397199999997
prime -> 6400 -> 46.0759346
prime -> 12800 -> 123.19425600000001
prime -> 25600 -> 353.01203510000005
prime -> 51200 -> 1037.8809906000001
prime -> 102400 -> 3079.4849928000003
prime -> 204800 -> 9097.821929499998

5 function calls in 0.155 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.155    0.155 <string>:1(<module>)
        1    0.155    0.155    0.155    0.155 lesson_4_task_2.py:71(prime)
        1    0.000    0.000    0.155    0.155 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log2}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

---- sieve
sieve -> 50 -> 0.05795579999903566
sieve -> 100 -> 0.15437919999931182
sieve -> 200 -> 0.3733611999996356
sieve -> 400 -> 0.8600688999995327
sieve -> 800 -> 2.182305800000904
sieve -> 1600 -> 4.254794599999514
sieve -> 3200 -> 9.279631400000653
sieve -> 6400 -> 24.251693400001386
sieve -> 12800 -> 59.16164000000026
sieve -> 25600 -> 138.81567369999902
sieve -> 51200 -> 332.1452416000011
sieve -> 102400 -> 745.7475567000001
sieve -> 204800 -> 1616.865541700001

7 function calls in 0.078 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.078    0.078 <string>:1(<module>)
        1    0.057    0.057    0.075    0.075 lesson_4_task_2.py:65(sieve)
        1    0.011    0.011    0.011    0.011 lesson_4_task_2.py:72(<listcomp>)
        1    0.007    0.007    0.007    0.007 lesson_4_task_2.py:81(<listcomp>)
        1    0.000    0.000    0.078    0.078 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log2}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

При условии роста n в два раза и при количестве повторений 10 000 раз, эффективность алгоритма Решето Эратосфена 
оказалась примерно в 1,5-2 раза выше, чем простой перебор и проверка чисел на простоту. И чем больше n, тем данная 
разница в эффективности выше.

При этом сложность алгоритма Решето Эратосфена, по моему мнению, близка к линейно-логарифмической О(n*(log n)²): 
при росте n в два раза, время на выполнение алгоритма растёт незначительно больше, чем в 2 раза, 
и с увеличением n данная разница будет расти всё медленнее.

Сложность же простого перебора чисел, по моему мнению, ближе к О((n*log n)**1.5): при росте n в два 
раза, время на выполнение алгоритма растёт больше, чем в 2 раза. Данная сложность больше заметна на больших n, 
т.к. увеличивается количество итераций без прерывания вложенного цикла. При этом при n <= ~15 000, сложность ближе 
к O(n**1.3*log n), т.к. вложенный цикл чаще прерываетсяи не проходит по всему массиву.

Соотвественно, т.к. (log n)² уменьшается быстрее, чем (log n*√(n*log n)), то и скорость выполнения алгоритма Решето 
Эратосфена также снижается быстрее. И при больших n разница будет сильнее заметна, что и показали тесты при n = 204 800,
 время выполнения алгоритма Решето Эратосфена примерно в 5,5 раза меньше простого перебора. 
При этом даже при небольших n и схожей асимптотической сложности обоих алгоритмов, время выполнения Решета Эратосфена 
в 2 раза ниже.
"""


def sieve(n):
    if n in {1, 2}:  # Принудительно добавляем число 2 и 3, которые не вошли в выборку
        return n + 1
    if n == 3:  # И число 5, которое тоже не вошло в выборку
        return 5

    end = int(n * math.log2(n) + 1)  # Вводим ограничение, исходя из модификации распределения простых чисел
    sieve = [num for num in range(end)]  # Создаем первоначальный список
    sieve[1] = 0

    for i, num in enumerate(sieve):
        if num:  # Проверяем есть ли число
            j = i * 2  # Число простое - увеличиваем его в 2 раза
            for k in range(j, end, i):  # Движемся по всем кратным числам
                sieve[k] = 0  # "Прокалываем" число

    return [num for num in sieve if num][n - 1]


def prime(n):
    start = 3  # Исключаем все чётные числа и 1
    end = int(n * math.log2(n) + 1)
    step = 2
    id_n = 1

    if n in {1, 2}:  # Но добавляем число 2 и 3, которые не вошли в выборку
        return n + 1
    if n == 3:  # И число 5, которое тоже не вошло в выборку
        return 5

    for num in range(start, end, step):
        is_prime = True
        max_div = int(num ** 0.5) + 1  # Делитель не больше квадратного корня

        for div in range(start, max_div, step):  # Начинаем с кратности 3 и шаг 2, т.к. чётных нет
            if not num % div:
                is_prime = False
                break

        if is_prime:  # Считаем количество простых чисел
            id_n += 1
        if id_n == n:
            return num


cProfile.run('prime(10411)')
cProfile.run('sieve(10411)')

n = 50
while n <= 204800:
    print('prime', n, timeit.timeit('prime(n)', globals=globals(), number=1000), sep=' -> ')
    n *= 2
n = 50
while n <= 204800:
    print('sieve', n, timeit.timeit('sieve(n)', globals=globals(), number=1000), sep=' -> ')
    n *= 2
