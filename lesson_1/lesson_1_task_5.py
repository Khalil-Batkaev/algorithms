# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв

char_1, char_2 = input('Введите две буквы через пробел: ').split()

x, y = ord(char_1) - 96, ord(char_2) - 96

if x >= y:
    print('Неверно введены данные')
else:
    z = y - x - 1
    print(f'Позиция первой буквы - {x}, позиция второй буквы - {y}, количество букв между ними - {z}')
