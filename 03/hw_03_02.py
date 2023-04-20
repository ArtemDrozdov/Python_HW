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

print(input_list)
print(f"Наиболее близкий элемент к {x}, является элемент {x_tmp}")
