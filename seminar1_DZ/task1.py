# Задача 2: Найдите сумму цифр трехзначного числа.

#num = "123"
# print(int(num[0])+int(num[1])+int(num[2]))

num = 111
result = 0
for i in range(1, 4):
    result = result + num % (10**i)//(10**(i-1))
print(result)