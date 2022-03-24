import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Определить, какое число в массиве встречается чаще всего

result_dict = {}
max_number = float('-inf')
max_value = 0

for num in array:
    if num not in result_dict:
        result_dict[num] = 1
    else:
        result_dict[num] += 1

for key, val in result_dict.items():
    if val >= max_value:
        max_number = key
        max_value = val

print(f'Чаще всего встречается число: {max_number}, повторений {max_value}')
