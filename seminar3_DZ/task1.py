# Подсчитать сколько раз встречается число k
list_1 = [1, 3, 3, 3, 5]
k = 3
counter = 0
for i in list_1:
    if i == k: counter += 1
print(counter)