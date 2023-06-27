# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
k = 'ноутбук'

ru_dict = dict()
ru_dict[1] = {'АВЕИНОРСТ'}
ru_dict[2] = {'ДКЛМПУ'}
ru_dict[3] = {'БГЁЬЯ'}
ru_dict[4] = {'ЙЫ'}
ru_dict[5] = {'ЖЗХЦЧ'}
ru_dict[8] = {'ШЭЮ'}
ru_dict[10] = {'ФЩЪ'}
en_dict = dict()
en_dict[1] = {'AEIOULNSTR'}
en_dict[2] = {'DG'}
en_dict[3] = {'BCMP'}
en_dict[4] = {'FHVWY'}
en_dict[5] = {'K'}
en_dict[8] = {'JX'}
en_dict[10] = {'QZ'}
score = 0
k = k.upper()
for i in k:
    for j in ru_dict.values():
        if i in str(j):
            key = [p for p in ru_dict if ru_dict[p] == j]
            score += key[0]
for i in k:
    for j in en_dict.values():
        if i in str(j):
            key = [p for p in en_dict if en_dict[p] == j]
            score += key[0]
print(score)

'''
# Предлагаемый вариант решения

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
'''