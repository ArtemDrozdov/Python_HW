# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться 
# в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

def rhythm(str):
    str = str.lower().split()
    lst = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        lst.append(result)
        # print(lst)
    return len(set(lst)) == 1
    # return len(lst) == lst.count(list[0])

str = input('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам\n')
# str = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# str = 'пара-ра-рам рам-пам-папам па-ра-па-дам-дам'

if rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')

# print(len(set(map(lambda part: len([w for w in part if w in 'аеёиоуыэюя']), song))) == 1)    