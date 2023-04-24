'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''
def degree(base_inp, degree_inp):
    if degree_inp == 0:
        return 1
    elif degree_inp == 1 :
        return base_inp
    else:
        return base_inp * degree(base_inp, degree_inp - 1)

a = int(input('Введите основание степени: '))
b = int(input('Введите степень числа: '))
print('Результат:', degree(a, b))