# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min = -50
max = 50

list_1 = [random.randint(-100,100) for i in range(11)]
print(list_1)
indexes = [i for i in range(len(list_1)) if min <= list_1[i] <= max]
print(indexes)
