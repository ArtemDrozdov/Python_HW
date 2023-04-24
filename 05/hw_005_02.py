'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*
2 2
    4 
'''
def summ(a, b):
    if b < 1 and a < 1:
        return 0
    elif a > 0 :
        return 1 + summ(a - 1, b)
    else:
        return 1 + summ(a, b - 1)

a = int(input('Введите a: '))
b = int(input('Введите b: '))
print('Результат:', summ(a, b))