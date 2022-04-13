from collections import Counter

"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) 
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно 
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего
"""

QUARTERS = 4

profit_comp = Counter()

qty = int(input('Введите количество предприятий: '))

for i in range(qty):
    name = input(f'Введите название {i + 1} компании: ')

    for quarter in range(QUARTERS):
        profit = float(input(f'Введите прибыль компании {name} за {quarter + 1} квартал: '))
        profit_comp[name] += profit

avrg_profit = round(sum(profit_comp.values()) / qty, 2)
id_more = 0

for _, profit in profit_comp.most_common():
    if profit >= avrg_profit:
        id_more += 1
    else:
        break

id_less = len(profit_comp) - id_more + 1

print(f'Средняя прибыль: {avrg_profit}')
print(f'Список компаний, чья прибыль выше среднего: {profit_comp.most_common(id_more)}')
print('--------')
print(f'Список компаний, чья прибыль ниже среднего: {profit_comp.most_common()[:-id_less:-1]}')

# альтернативный вывод, более красивый

# print(f'Список компаний, чья прибыль выше среднего:')
# for name, profit in profit_comp.most_common():
#     if profit >= avrg_profit:
#         print(name, profit, sep=' - ')
#     else:
#         break
# print('--------')
# print(f'Список компаний, чья прибыль ниже среднего:')
# for name, profit in profit_comp.most_common()[::-1]:
#     if profit < avrg_profit:
#         print(name, profit, sep=' - ')
#     else:
#         break
