'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
         0  1  2  3   4   5  6  7   8   9 10 11  12 13  14  15 16  17  18 19
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
диапазон 7 - 10 ?
Вывод: [1, 9, 13, 14, 19]
'''

# str = input("Введите через пробел элементы списка: ").split()
str = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
numb_min = 7 # input("Минимальное значение диапазона поиска: ")
numb_max = 10 # input("Максимальное значение диапазона поиска: ")
str_idx = []
# cnt = 0

# for item in str:
#     if numb_min <= item <= numb_max :
#         str_idx.append(cnt)
#     cnt += 1
for item in range(len(str)):
    if numb_min <= str[item] <= numb_max :
        str_idx.append(item)

print(str)
print(str_idx)

# # эталонное
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
# min_number = int(input()) 
# max_number = int(input()) 
# for i in range(len(list_1)): 
#     if min_number <= list_1[i] <= max_number: 
#         print(i)