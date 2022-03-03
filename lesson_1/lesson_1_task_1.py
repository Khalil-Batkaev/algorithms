number = int(input('Введите трехзначное число: '))
digit_1 = number // 100
digit_2 = number % 100 // 10
digit_3 = number % 10
print(f'Сумма чисел = {digit_1 + digit_2 + digit_3}, а произведение = {digit_1 * digit_2 * digit_3}')