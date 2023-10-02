from logger import input_contact, print_contacts, find_contact,delete_contact,change_contact


def menu():
    text = '' \
           "Главное меню:\n" \
           "1. Добавить контакт\n" \
           "2. Посмотреть все контакты\n" \
           "3. Найти контакт\n"\
           "4. Изменить контакт\n"\
           "5. Удалить контакт\n"\
           "6. Выход\n"
    print(text)
    while True:
        try:
            comand = int(input('Введите команду: \n'))
        except ValueError:
            print('Вы ввели не число!')
        else:
            if comand == 1:
                input_contact()
            if comand == 2:
                print_contacts()
            if comand == 3:
                find_contact()
            if comand == 4:
                change_contact()
            if comand == 5:
                delete_contact()
            if comand == 6:
                print('Всего доброго!')
                break
            print('_' * 30)


if __name__ == '__main__':
    menu()
