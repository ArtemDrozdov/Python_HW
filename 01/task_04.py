###########################################################################
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def dolki(n = input(f"Введите N: "), m = input(f"Введите M: "), k = input(f"Введите K долек отломленых: ")):
    n_tmp, m_tmp, k_tmp = int(n), int(m), int(k)
    if (k_tmp < n_tmp * m_tmp) and  ( ((k_tmp % n_tmp) == 0) or ((k_tmp % m_tmp) == 0) ):
        return 'YES'
    else:
        return 'NO'

print(dolki())