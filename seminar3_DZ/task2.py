# Требуется найти в массиве list_1
# самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 2, 3, 4, 5]
k = 6
min = k - list_1[0]
flag = 0
for i in list_1:
    if abs(k-i) <= abs(min):
        min = k - i
        flag = i
print(flag)