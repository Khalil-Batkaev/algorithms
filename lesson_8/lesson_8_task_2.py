from collections import Counter, deque

"""
Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""


# Создаем класс Узел
class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'left = > {self.left} - right => {self.right}'


# Построение дерева по алгоритму Хаффмана
def hm_tree(data):
    # Создаём массив отсортированных по возрастанию повторений символов строки
    spam = deque(Counter(data).most_common()[::-1])

    for _ in range(len(spam) - 1):
        # Берём по два элемента с минимальным весом
        char_left, val_left = spam.popleft()
        char_right, val_right = spam.popleft()

        res = val_left + val_right  # Считаем их совокупный вес
        node = MyNode(char_left, char_right)  # Записываем символы в виде узла

        for i, item in enumerate(spam):
            _, val = item
            if val >= res:  # Добавляем наш узел в массив согласно новому весу
                spam.insert(i, (node, res))
                break
        else:  # Если вес самый большой, то в конец массива
            spam.append((node, res))

    return spam[0][0]  # Возвращаем полученное дерево без веса


# Определение кодировки символов
def hm_encode(node, path=''):
    encodings = {}
    # Если это не узел, то добавляем символ с его кодировкой в словарь
    if isinstance(node, str):
        return {node: path}
    # Определяем код по накопленному пути налево +0
    encodings.update(hm_encode(node.left, path=f'{path}0'))
    # И пути направо +1
    encodings.update(hm_encode(node.right, path=f'{path}1'))

    return encodings


text = 'beep boop beer!'

encoding = hm_encode(hm_tree(text))

print(f'Текст "{text}" в кодировке Хаффмана выглядит так: ', end='')
for char in text:
    print(encoding[char], end='')
    if char == ' ':
        print(end=' ')
