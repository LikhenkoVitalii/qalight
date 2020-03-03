import sys


def menu():

    print("\n 1.Создать запись\n 2.Найти запись\n 3.Редактировать запись\n 4.Удалить запись\n 5.Выйти из программы\n")
    print("Введите значение от 1 до 5:")
    get = input()

    while get:

            if get == '1':
                print("Создать запись")
                pass
                break

            elif get == '2':
                print("Найти запись")
                pass
                break

            elif get == '3':
                print("Редактировать запись")
                pass
                break

            elif get == '4':
                print("Удалить запись")
                pass
                break

            elif get == '5':
                 sys.exit()

            else:
                print("Неверный ввод")
                print("Введите значение от 1 до 5:")
                get = input()



menu()
