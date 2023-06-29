# def sum_numbers(n):
#     summa = 0
#     for i in range(1,n+1):
#         summa += i
#     print(summa)
# sum_numbers(5)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1,n+1):
#         summa += i
#     return(summa)
#
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n, y = 'Hello'):
#     summa = 0
#     print(y)
#     for i in range(1,n+1):
#         summa += i
#     return(summa)
#
# a = sum_numbers(5, 'qwert')
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','r','5','76'))



# ------------------------ модульность
# import module1
# print(module1.max1(5,0))

# from module1 import max1
# print(max1(5,0))

# import module1 as m1
# print(m1.max1(5,0))


# ------------------------ Рекурсия

# Пользователь вводит n и надо вывести первые n чисел последовательности фибоначчи
# from module2 import fib
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)
