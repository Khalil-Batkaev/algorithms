from hashlib import sha1

"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется 
вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

>>> func("papa")
6
>>> func("sova")
9
"""

"""
Долго думал, прикладывать ли это решение...рискнул :)
Ничего интересного с хешами не придумалось. Решение аналогичное строковому перебору.
Единственное, в чём я вижу оптимизацию - экономия памяти: хеш занимает намного меньше места.
"""

# Решение без хеша для проверки
def get_unique_sub(data):
    unique_sub = set()
    limit_i = len(data)
    limit_j = len(data) + 1
    is_first = True

    for i in range(limit_i):
        k = i + 1

        for j in range(k, limit_j - 1 if is_first else limit_j):
            unique_sub.add(data[i:j])
        is_first = False

    return len(unique_sub)


def get_unique_sub_hash(data):
    limit_i = len(data)
    limit_j = len(data) + 1
    unique_sub = set()

    for i in range(1, limit_i):
        for j in range(limit_j - i):
            sub = sha1(data[j:j + i].encode('utf-8')).hexdigest()
            unique_sub.add(sub)

    return len(unique_sub)


text = 'papa'
print(f'Количество уникальных подстрок в строке {text} составляет {get_unique_sub_hash(text)}')
