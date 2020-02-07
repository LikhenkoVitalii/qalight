import random

print("Введите количество элементов первого списка:")
a = int(input())
print("Введите количество элементов второго списка:")
c = int(input())


def gettext(a, c):

    if a <= 0:
        print("Неверное значение")
        print("Введите количество элементов первого списка:")
        a = int(input())
    else:
        print("Введите максмальное значение первого списка:")
        b = int(input())

    if c <= 0:
        print("Неверное значение")
        print("Введите количество элементов второго списка:")
        c = int(input())
    else:
        print("Введите максмальное значение второго списка:")
        d = int(input())
    list1 = []
    for l in range(a):
        l = int(random.randint(0, b))
        list.append(l)
    print(list1)
    list2 = []
    for f in range(c):
        f = int(random.randint(0, d))
        list.append(f)
    print(list2)
    list3 = list(set(list1) & set(list2))
    return print(list3)
print (gettext(a, c))
