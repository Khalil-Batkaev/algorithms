"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры
"""


def func(n, k=1.0):

    if n == 1:
        return k
    if n > 1:
        res = func(n - 1, k / 2)
        if n % 2:
            return f'{k} {res}'
        return f'{k} -{res}'


n = int(input('Введите n: '))

if n > 1:
    print(sum(map(float, func(n).split())))
else:
    print(n)
