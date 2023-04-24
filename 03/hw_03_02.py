"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В 
последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""

length_list = int(input("Введите длину списка N: "))
x = int(input("Введите искомое число: "))
x_tmp = 0
x_delta_tmp = 2147483647 # максимальное число integer

input_list = []

for i in range(length_list):
    # input_list.extend(int(input(f"Введите элемент списка {i}: "))) 
    # TypeError: 'int' object is not iterable \\ уточнить у преподавателя!
    input_list.append(int(input(f"Введите элемент списка {i}: ")))
    if (abs(x - input_list[i])) < x_delta_tmp :
        x_tmp = input_list[i]
        x_delta_tmp = abs(x - input_list[i])

# ======================================================================================
# ======================================================================================

# print(input_list)
# print(f"Наиболее близкий элемент к {x}, является элемент {x_tmp}")

# n = int(input('Введите количество элементов списка: '))
# str = input("Введите через пробел элементы списка: ").split()
# list = []
# for i in str:
#     list.append(int(i))
# x = int(input('Введите число x, c которым нужно сравнить элементы в списке: '))
# dif_min = abs(x - list[0])
# close_element = list[0]
# for item in range(n):
#     if list[item] == x:
#         break
#     if abs(x - list[item]) < dif_min:
#         dif_min = abs(x - list[item])
#         close_element = list[item]
# print(f'Самый близкий по величине элемент {close_element}')

