# Функция чтения файла
def open_book():
    with open('Phonebook/phonebook.txt', 'r') as f:
        list_contact = f.read().splitlines()
    number = 0
    for i in list_contact:
        number += 1
        print(number,i)
    
    user_menu()

# Функция поиска контакта по имени
def search_by_name():
    search_name = input('Введите фамилию, имя или отчество: ')
    search = False

    with open('Phonebook/phonebook.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if search_name in str(line):
                print(line)
                search = True

    if search == False:
        print('Контакт с таким именем не найден')

    user_menu()

# Функция поиска контакта по номеру телефона
def search_by_number():
    search_number = input('Введите номер телефона: ')
    search = False

    with open('Phonebook/phonebook.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if search_number in str(line):
                print(line)
                search = True

    if search == False:
        print('Контакт с таким номером телефона не найден')

    user_menu()

# Функция добавления контакта в файл
def add_new_contact():
    contact_list = []
    contact_list.append(input('Введите фамилию: '))
    contact_list.append(input('Введите имя: '))
    contact_list.append(input('Введите отчество: '))
    contact_list.append(input('Введите номер телефона: '))

    with open('Phonebook/phonebook.txt', 'a') as f:
        f.write((' '.join(contact_list)))
    print('Контакт успешно добавлен')

    user_menu()

# Функция удаления контакта из файла
def del_contact():
    with open('Phonebook/phonebook.txt', 'r') as f:
        list_contact = f.read().splitlines()
    number = 0

    for i in list_contact:
        number += 1
        print(number,i)

    del_contact = int(input('Введите порядковый номер контакта: '))

    f = open('Phonebook/phonebook.txt').readlines()
    f.pop(del_contact-1)
    with open('Phonebook/phonebook.txt', 'w') as F:
        F.writelines(f)
    print('Контакт успешно удален')

    user_menu()

# Пользовательское меню
def user_menu():
    user_choice = int(input('\nВВЕДИТЕ НОМЕР ПУНКТА ИЗ МЕНЮ\n'
        '1. Показать все записи\n'
        '2. Найти запись по вхождению частей имени\n'
        '3. Найти запись по телефону\n'
        '4. Добавить новый контакт\n'
        '5. Удалить контакт\n'
        '6. Выход\n'))
    print('')
        

    if user_choice == 1:
        open_book()
    if user_choice == 2:
        search_by_name()
    if user_choice == 3:
        search_by_number()
    if user_choice == 4:
        add_new_contact()
    if user_choice == 5:
        del_contact()
    if user_choice == 6:
        exit()

user_menu()