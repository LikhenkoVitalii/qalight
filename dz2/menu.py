import sys


def menu():
    print("\n 1.Создать запись\n 2.Найти запись\n 3.Редактировать запись\n 4.Удалить запись\n 5.Выйти из программы\n")
    print("Введите значение от 1 до 5:")
    get = input()

    if get == '1':
        print("Создать запись")
        pass

    elif get == '2':
        print("Найти запись")
        pass

    elif get == '3':
        print("Редактировать запись")
        pass

    elif get == '4':
        print("Удалить запись")
        pass

    elif get == '5':
        sys.exit

    else: print("Неверный ввод")


menu()
