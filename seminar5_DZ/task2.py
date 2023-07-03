# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def summ(a,b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a > 0 and b > 0:
        return summ(a+1, b-1)
    if b < 0 and a < 0:
        return summ(a-1, b+1)
    if a > 0 and b < 0:
        return summ(a-1, b+1)
    if a < 0 and b > 0:
        return summ(a+1, b-1)
print(summ(5,-2))