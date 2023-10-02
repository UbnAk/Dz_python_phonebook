import os

def input_contact():
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()
    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').lower().strip().split()
        f.write(';'.join(user) + '\n')
        print('Контакт успешно добавлен!')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    print()
    print("_"*30)
    for contact in contacts:
        print(*contact.title().strip().split(';'))
    print('Список контактов успешно загружен!')


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ').lower()
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            result = ' '.join(full_contact)
            print(result)

def delete_contact():
    delete = False
    new_contacts = []
    while True:
        print('По каким параметрам удалим контакт?:\n1. Имя\n2. Фамилия\n3. Телефон\n')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    name_del = input('Введите данные: ').lower()
    with open('data.txt', 'r', encoding='utf-8') as f:
        for contact in f:
            info_contact = contact.strip().split(';')
            if info_contact[command_index-1] != name_del:
                new_contacts.append(contact)
            else:
                delete = True
    with open('data.txt', 'w', encoding='utf-8') as f:
        for contact in new_contacts:
            f.write(contact)
    if delete:
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден.")




def change_contact():
    new_str = []
    delete = True
    new_phone_book = []
    print('Какие параметры будем менять у контакта?:\n1. Имя\n2. Фамилия\n3. Телефон\n')
    while True:
        command_index = int(input('Введите команду: '))
        if str(command_index) not in '123':
            print('Других параметров нету.\nВыберите пункт из предложенных вариантов\n1. Имя\n2. Фамилия\n3. Телефон\n')
        else:
            break
    name_del = input('Введите данные: ').lower()
    with open('data.txt', 'r', encoding='utf-8') as f:
        for contact in f:
            info_contact = contact.strip().split(';')
            if name_del != info_contact[command_index-1]:
                new_phone_book.append(contact)
            else:
                for i in info_contact:
                    if i == name_del:
                        i = input('Введите новые данные: ').lower()
                        new_str.append(i)
                    else:
                        new_str.append(i)
                new_phone_book.append(';'.join(new_str)+'\n')

    with open('data.txt', 'w', encoding='utf-8') as f:
        for contact in new_phone_book:
            f.write(contact)
    if delete:
        print("Контакт успешно изменен!")
    else:
        print("Контакт не изменен")
