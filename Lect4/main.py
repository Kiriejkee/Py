# def f(x):
#     return x*x
# a = f
# print(a(2))
# print(f(2))

# def calc1(a, b):
#     return a+b

# def calc2(a, b):
#     return a*b
#
# def math(op, x, y):
#     print(op(x,y))
#
# math(lambda a,b: a+b,4,5)
# -----------
# LAMBDA
# ran = [1,2,3,5,8,15,23,38]
# result = [(i,i**2) for i in ran if i%2==0]
# print(result)

# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# res = select(int, ran)
# print(res)
# res = where(lambda x: x % 2 ==0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)
# ---------------------
# MAP

# list_1 = [x for x in range(1,20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)
# -----------------------------


# data = '15 152 12 536 123 777 22'
# print(data)
#
# # data = data.split()
# # print(data)
#
# data = list(map(int, data.split()))
# print(data)
# -------------------------------
#
# FILTER
# data = [1,2,3,5,8,15,23,38,1855]
# res = list(filter(lambda x: x%10 == 5, data))
# print(res)


# --------------------------------

# ran = [1,2,3,5,8,15,23,38]
# # result = [(i,i**2) for i in ran if i%2==0]
# # print(result)
#
# # def select(f, col):
# #     return [f(x) for x in col]
# #
# # def where(f, col):
# #     return [x for x in col if f(x)]
#
# res = map(int, ran)
# res = filter(lambda x: x % 2 ==0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# --------------------------------------
# ZIP возвращает список из кортежей по минимальному вхождению

# usr = [ 'usr1', 'usr2', 'usr3']
# id = [1, 4, 5, 6]
# name = ['Jenya', 'Nastya', 'Cody']
#
# list_1 = list(zip(usr, id, name))
# print(list_1) #[('usr1', 1, 'Jenya'), ('usr2', 4, 'Nastya'), ('usr3', 5, 'Cody')]



# -------------------------------
# ENUMERATE нумерует итерируемый объект
# name = ['Jenya', 'Nastya', 'Cody']
# list_1 = list(enumerate(name))
# print(list_1) #[(0, 'Jenya'), (1, 'Nastya'), (2, 'Cody')]



# -----------------------------

# Работа с файлами
# Варианты режима (мод):
# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
#    и в него начнется запись.
# r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа
#    выдаст ошибку.
# w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.
#
# Миксованные режимы:
# 1. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 2. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')

# Модуль SHUTIL - библиотека для работы с папками/файлами
# Модуль OS - библиотека для работы с операционной системой