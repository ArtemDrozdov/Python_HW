# ### ### ### ### ### ### ### ### ### ###
# Задача №49. Решение в группах
# Создать  телефонный  справочник  с возможностью  импорта  и  экспорта  данных  в 
# формате  .txt.  Фамилия,  имя,  отчество,  номер телефона - данные, которые должны находиться 
# в файле.
# 1. Программа должна выводить данные
# 2. Программа  должна  сохранять  данные  в текстовом файле
# 3. Пользователь  может  ввести  одну  из характеристик  для  поиска  определенной 
# записи(Например  имя  или  фамилию человека)
# 4. Использование  функций.  Ваша  программа не должна быть линейной
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
# данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных

import os
import shutil

# os.chdir("D:/EDU_PROJECTS/Python_Seminar/08")
# print(os.getcwd())

FILE_PATH = r'phone_contact.txt'
FILE_PATH_TMP = r'phone_contact_tmp.txt'
# CONST_

# with open(FILE_PATH, 'w', encoding='utf-8') as f:
#     for i in range(1,5):
#         f.write(f'\nИванов{i},Иван{i},Иванович{i},{111**i}')
#     for i in range(1,5):
#         f.write(f'\nСидоров{i},Кесарь{i},Петрович{i},{222**i}')

##################################################################
# функции
def info_menu():
    print("\nИнструкция:")
    print("[1]. Показать весь справочник")
    print("[2]. Добавить контакт")
    print("[3]. Поиск по справочнику")
    print("[4]. Редактировать контакт")
    print("[5]. Удалить контакт")
    print("[0]. Выход\n")
#
def show_all_contact():
    print("Весь справочник: ")
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
#
def add_contact():
    surname  = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    with open(FILE_PATH, 'a', encoding='utf-8') as f:
        f.write('\n'+ surname + ',' + name + ',' + patronymic + ','+ phone)
#
def search_contact():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        search = input("Какой атрибут контакта ищем: ")
        search_flag = False
        for line in f:
            if search in line:
                print(line.strip())
                search_flag = True
        if search_flag == False:
            print("Нет такого сочетания")
#
def comp_pole(a, b):
    return b if a == '.' else a
    

def edit_contact():
    idx = int(input("Введите индекс изменяемой строки контакта: "))
    print("Если необходимо сохранить старую запись в поле, поставьте точку")
    surname  = input("Введите новую фамилию: ")
    name = input("Введите новое имя: ")
    patronymic = input("Введите новое отчество: ")
    phone = input("Введите новый телефон: ")
    lst_tmp = []
    with open(FILE_PATH, 'r', encoding='utf-8') as f1:
        with open(FILE_PATH_TMP, 'w', encoding='utf-8') as f2:
            flag_edit = False
            # print(f'дебаг\ idx: {idx}')
            i = 0
            while not flag_edit:
                info = f1.readline()
                # print(f'дебаг\ i: {i}')
                # print(f'дебаг\ info: {info}')
                lst_tmp = info.strip().split(sep=",")
                # print(lst_tmp)
                # print("surname")
                if info:
                    if idx == i:
                        f2.write(comp_pole(surname, lst_tmp[0])  + ',' 
                                 + comp_pole(name, lst_tmp[1]) + ',' 
                                 + comp_pole(patronymic, lst_tmp[2]) + ','
                                 + comp_pole(phone, lst_tmp[3]) + "\n")                        
                    else:
                        f2.write(info)
                else:
                    flag_edit = True
                i += 1
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TMP, FILE_PATH)
#
def delete_contact():
    inx = int(input("Введите индекс удаляемой строки контактов: "))
    with open(FILE_PATH, 'r', encoding='utf-8') as f1:
        with open(FILE_PATH_TMP, 'w', encoding='utf-8') as f2:
            flag_del = False
            i=0
            while not flag_del:
                info = f1.readline()
                if info:
                    if inx != i:
                        f2.write(info)
                else:
                    flag_del = True
                i+=1
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TMP,FILE_PATH)

##################################################################
# вызов справочника
while True:
    info_menu()
    choice = input("Введите номер действия: ")       
    match choice:
        case "1": # "[1]. Показать весь справочник"
            show_all_contact()
        case "2": # "[2]. Добавить контакт"
            add_contact()
        case "3": # "[3]. Поиск по справочнику"
            search_contact()
        case "4": # "[4]. Редактировать контакт"
            edit_contact()
        case "5": # "[5]. Удалить контакт"
            delete_contact()
        case "0": # "[0]. Выход\n"
            break
        case _: # ничего не подошло
            print("Неправильно ввели действие")



##################################################################
    # lst = []
    # with open(FILE_PATH, 'r', encoding='utf-8') as f:
    #     lst = list(map(lambda x: x.strip(),f.readlines()))
    #     print(f'Список контактов: \n{lst}')
        
    #     print(len(lst))

    #     # idx = lst.index("Сидоров1,Кесарь1,Петрович1,222")
    #     idx = lst.index((search))
    #     print(idx)

    #     # print(list(f.readlines()).len)
    #     # print(f'Индекс атрибута: {list(map(lambda x: x.index(search),f.readlines()))}')
