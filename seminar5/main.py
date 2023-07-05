# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1


# score_list = [1, 3, 3, 3, 4]
# print(score_list)
#
# new_score_list = []
#
# for i in score_list:
#     if i == max(score_list):
#         new_score_list.append(min(score_list))
#     else:
#         new_score_list.append(i)
#
# print(new_score_list)
#
#
# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)
#
# max_number = max(list_1)
# min_number = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_number:
#         list_1[i] = min_number
# print(list_1)


# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# def isPrime(n, delim=2):
#     if n < 2:
#         return False
#     if n == 2 or delim * delim > n:
#         return True
#     if n % delim == 0:
#         return False
#     return isPrime(n, delim + 1)
#
#
# print(isPrime(4))


# Задача No37. Решение в группах
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

# def rev(N):
#     if N==0:
#         return
#     item = int(input(f'Элемент {n}'))
#     rev(N-1)
#     print(item)

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f' {k}'
#
#
# n = int(input())
# print(f(n))

# -----------палиндромность

# def polindrom(word):
#     if len(word) < 2:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     return polindrom(word[1:-1])
#
# print(polindrom("арозаупаланалапуазора"))