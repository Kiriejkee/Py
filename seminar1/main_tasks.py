# Ввести два числа с консоли и определить какое из них больше
# num1 = int(input("Введите 1-е число "))
# num2 = int(input("Введите 2-е число "))
#
# if num1 > num2:
#     print(f"Первое число = {num1} больше чем второе")
# elif num2 > num1:
#     print(f"Второе число = {num2} больше чем первое")
# else:
#     print("Equal")
#
# Задача No1. Решение в группах
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией
# if и циклами.
# Input:
# n = 700 m = 750 Output: 2

# n = int(input("ведите количество километров в день "))
# m = int(input("Введите длину пути "))
# print(f"Необходимо {m // n+(m % n != 0)} дней")
# print(f"{(m+n-1)//n}")


# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# c1 = 20
# c2 = 21
# c3 = 22
# a = (c1 + 1)//2
# b = c2//2 + (c2 % 2 != 0)
# c = (c3 + 1)//2
# print()

# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным.
# Если год является високосным, то выведите YES,
# иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.
# Input: 2016 Output: YES

# year = 2019
#
# if (year % 4 ==0) and (year % 100 !=0) or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# Задача No5. Общее обсуждение
# 5.Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того,
# в какую сторону едет электричка).
# В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите программу,
# которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6

i = 3
j = 4

if i != j :
    print(i+j-1)
else: print("Недостаточно информации")