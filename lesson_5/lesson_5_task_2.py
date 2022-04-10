from collections import deque

"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число 
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить 
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

DIGITS_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
             'D': 13, 'E': 14, 'F': 15}
DIGITS_10 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
BASE = 16


def sum_digit_16(num_1, num_2):

    result = deque()

    if len(num_1) > len(num_2):
        num_1, num_2 = list(num_1), deque(num_2)
        num_2.extendleft(['0'] * (len(num_1) - len(num_2)))
    elif len(num_1) < len(num_2):
        num_1, num_2 = deque(num_1), list(num_2)
        num_1.extendleft(['0'] * (len(num_2) - len(num_1)))
    else:
        num_1, num_2 = list(num_1), list(num_2)

    n = len(num_1)
    _one = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        res_digit = DIGITS_16[num_1[i]] + DIGITS_16[num_2[i]] + _one[i]

        if res_digit >= BASE:
            res_digit -= BASE
            result.appendleft(DIGITS_10[res_digit])
            _one[i - 1] = 1
            if not i:
                result.appendleft('1')
        else:
            result.appendleft(DIGITS_10[res_digit])

    return f'Результат сложения числе = {result}'


number_1 = input('Введите первое число: ').upper()
number_2 = input('Введите второе число: ').upper()

print(sum_digit_16(number_1, number_2))
