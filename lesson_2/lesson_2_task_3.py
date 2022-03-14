"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843
"""


def rev_number(number):

    if 0 <= number < 10:
        return number
    else:
        digit = number % 10
        number = rev_number(number // 10)
        return f'{digit}{number}'


num = int(input('Введите натуральное число: '))
print(int(rev_number(num)))
