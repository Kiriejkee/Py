from tabulate import tabulate


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента\n"
          "7. Изменить данные абонента\n"
          "8. Закончить работу")
    choice = int(input())
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')


    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print_table(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print_table(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice == 6:
            name = get_delete_name()
            delete(phone_book, name)
            write_csv('phonebook.csv', phone_book)
        elif choice == 7:
            data = get_change_data(phone_book)
            change_name(data,phone_book)
            write_csv('phonebook.csv', phone_book)
        choice = show_menu()


def get_delete_name():
    return input("Введите имя или фамилию абонента для удаления: ")


def delete(phone_book, name):
    flag = 1
    while flag:
        for i in phone_book:
            if i["Фамилия"] == name or i["Имя"] == name:
                check = input(f'\n{i}\n Если вы хотите удалить абонента введите 1, иначе нажмите Enter')
                if check:
                    phone_book.remove(i)
                    print(f'Абонент {name} удалён из справочника')
                flag = 0
        if flag == 1:
            print("Абонент с таким именем или фамилией не найден")
        flag = 0


def get_change_data(phone_book):

    choice = int(input("Если хотите изменить фамилию абонента введите - 0, если имя - введите 1: "))
    if choice == 0:
        choice = "Фамилия"
        staroe = input("Введите старую фамилию абонента: ")
        if find_by(phone_book, choice, staroe) == 'Контакт не найден :(': return False
        name = input("Введите новую фамилию абонента: ")

    elif choice == 1:
        choice = "Имя"
        staroe = input("Введите старое имя абонента: ")
        if find_by(phone_book, choice, staroe) == 'Контакт не найден :(': return False
        name = input("Введите новое имя абонента: ")
    # else:
    #     return get_change_data(phone_book)
    return [choice, staroe, name]


def change_name(data, phone_book):
    if data == False: return print('Контакт не найден :(')
    else:
        for i in phone_book:
            if i[data[0]] == data[1]:
                i[data[0]] = data[2]
                return print("Данные успешно изменены! ")




def print_result(phone_book):
    print_table(phone_book)


def print_table(data):
    print(tabulate(data, headers='keys', tablefmt='pipe', stralign='center'))


def get_search_name():
    return input('Введите Фамилию контакта: ').lower()


def find_by_name(phone_book, name):
    return find_by(phone_book, "Фамилия", name)


def find_by_number(phone_book, number):
    return find_by(phone_book, "Телефон", number)


def get_search_number():
    return input('Введите номер телефона контакта: ')



def find_by(phone_book, case, data):
    result = list()
    for i in phone_book:
        if i[case].lower() == data.lower():
            result.append(i)
    if len(result) == 0:
        return 'Контакт не найден :('
    else:
        return result



def get_new_user():
    new_usr = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
    for i in new_usr.keys():
        new_usr[i]=input(f'Введите {i.lower()} контакта :')
    return new_usr


def add_user(phone_book, user_data):
    phone_book.append(user_data)

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(','))) # strip режет символы (по умолчанию пробел, как в сплите)
            data.append(record)
    return data


def get_file_name():
    return input("Введите имя файла: ")


def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')
    print(f"Справочник успешно записан в {filename}")

work_with_phonebook()
