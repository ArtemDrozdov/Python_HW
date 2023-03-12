###########################################################################
# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Решение-1 с использование математического подхода и цикла While
def sumElemWhile(number = input("Введите целое число: ")):
    numb = int(number)
    sum_el = 0
    while (numb > 0):
        sum_el += numb % 10
        numb = numb // 10   # важно поставить деление нацело, иначе будут доли
        # print(type(numb))
    return sum_el
print(f"Cумма цифр = {sumElemWhile()}")

# Решение-2 без использования математичского подхода
def sumElem(number=input('Введите трехзначное число: ')):
    return int(number[0]) + int(number[1]) + int(number[2])
print(f"Cумма цифр = {sumElem()}")

# Решение-3 с использование математического подхода и цикла for
def sumElemFor(number=input('Введите целое число: ')):
    numb = int(number)
    sum_el = 0
    for i in range(len(number)):
        sum_el += numb % 10
        numb = numb // 10
    return sum_el
print(f"Cумма цифр = {sumElemFor()}")