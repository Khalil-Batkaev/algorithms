# Пользователь вводит номер буквы в алфавите. Определить, какая это буква

x = int(input('Введите номер буквы от 1 до 26: '))
y = chr(x + 96)

print(y)