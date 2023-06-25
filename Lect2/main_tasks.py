# #Создание списка
# # list_1 = []
# # list_1 = list()
# # list_1 = [1, 2, 3, 5]
# # print(list_1)
# # print(*list_1)
#
# # for i in list_1:
# #     print(i)
#
# # print(len(list_1))
# # print(list_1[0]) Вывод элемента листа (при "-" нумерация с конца)
#
# # list_1 = [1, 5]
# # print(list_1)
# # list_1.append(8) Добавление элемента
# # print(list_1)
# # list_1.append(85)
# # print(list_1)
#
# # list_1 = []
# # print(list_1)
# # for i in range(5):
# #     list_1.append(i)
# #     print(list_1)
#
# # list_1 = [12, 7, 1, 8 ,9]
# # print(list_1.pop(1))
# # print(list_1)
# #
# # print(list_1.insert(2,11))
# # print(list_1)
# #
# # print(list_1[0])
# # print(list_1[-1])
# # print(list_1[:])
# # print(list_1[:2])
# # print(list_1[len(list_1)-1:2])
# # print(list_1[1:4])
# # print(list_1[1:-3])
# # print(list_1[0:4:2])
# # print(list_1[::6])
#
# # кортежи
# # t = ()
# # print(type(t))
# #
# # t=(1, 5, 3,)
# # print(type(t))
# #
# # v = [1, 8, 9]
# # print(v)
# # print(type(v))
# #
# # v = tuple(v)
# # print(v)
# # print(type(v))
# #
# #
# # a, b, c = v
# # print(a, b, c)
#
# # t = (1, 2, 3, 4, 5)
# # for i in range(len(t)):
# #     print(t[i])
#
# # t[0] = 2 -- изменение итема не возможно
# # print(t)
#
# # Словари - можем сами задавать ключ
#
# # d = {}
# # d = dict()
# #
# # d['q'] = "qwerty"
# # print(d)
# #
# # d['w'] = 'werty'
# # print(d)
# # print(d['q'])
# #
# # d[22] = 223
# # print(d)
# #
# # del d[22]
# # print(d)
# #
# # for i in d:
# #     # print(i)
# #     print('{}: {}'.format(i,d[i]))
# #
# # for (k,v) in d.items():
# #     print(k,v)
# #
# # print(d.items())
#
# # Множества - содержит только уникальные
#
# num = {1, 2, 4, 5}
# print(num)
# #
# # num.add(2)
# # print(num)
# #
# # num.add(0)
# # print(num)
# #
# # num.add(3)
# # print(num)
# #
# # num.remove(5) #нельзя удалить не существующее
# # print(num)
# #
# # num.discard(5) #ищет есть ли и если есть удаляет
# # print(num)
# #
# # num.clear()
# # print(num)
#
# # num_2 = {2, 3, 6, 10}
# # print(num_2)
# # c = num_2.copy()
# # print(c)
# #
# # u = num.union(num_2)
# # print(u)
# #
# # i = num.intersection(num_2)
# # print(i)
# #
# # d1 = num.difference(num_2)
# # print(d1)
# #
# # d2 = num_2.difference(num)
# # print(d2)
#
# a = {1, 8, 6}
#
# b = frozenset(a) #создание неизменяемого множества
#
# print(b)