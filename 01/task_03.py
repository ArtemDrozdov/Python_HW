###########################################################################
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# простой вариант
def ticketLuckySimple(number=input("Введите номер билета: ")):
    return (int(number[0]) + int(number[1]) + int(number[2])) == (int(number[3]) + int(number[4]) + int(number[5]))
print(f"Счастливость >> {'YES' if (ticketLuckySimple() == True) else 'NO'}")

# вариант с вызовом мат. функцций
def ticketLuckyFloat(number=input("Введите номер билета: "), idx=input("Введите номер индекса сравнения (отсчет с 0 и с права на лево): ")):
    numb = int(number)
    sum_1 = 0
    sum_2 = 0
    for i in range(len(number)):
        if i < int(idx):
            sum_1 += numb % 10
            # print(f"sum_1 = {sum_1}")
        else:
            sum_2 += numb % 10
            # print(f"sum_2 = {sum_2}")
        numb = numb // 10
    return 'YES' if sum_1 == sum_2 else 'NO'

print(f"Счастливость >> {ticketLuckyFloat()}")
