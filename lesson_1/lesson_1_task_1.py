# https://drive.google.com/file/d/1gg_x4qJllbpzSqYSxZLPEIYFn6IDegHe/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

number = int(input('Введите трехзначное число: '))
digit_1 = number // 100
digit_2 = number % 100 // 10
digit_3 = number % 10
number_sum = digit_1 + digit_2 + digit_3
number_multi = digit_1 * digit_2 * digit_3
print(f'Сумма чисел = {number_sum}, а произведение = {number_multi}')
