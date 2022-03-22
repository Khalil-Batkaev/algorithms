# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

MIN_DIVISOR = 2
MAX_DIVISOR = 9
MIN_NUMBER = 2
MAX_NUMBER = 99

for divisor in range(MIN_DIVISOR, MAX_DIVISOR + 1):
    count = 0
    for number in range(MIN_NUMBER, MAX_NUMBER + 1):
        if not number % divisor:
            count += 1
            
    print(f'У делителя {divisor} количество кратных чисел равно {count}')
