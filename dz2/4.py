import random

print("Введите количество элементов списка:")
a = int(input())
print("Введите максмальное значение списка:")
b = int(input())


def listfunction(a, b):
    list1 = []
    for l in range(a):
        l = random.randint(1, b)
        list1.append(l)
    return list1


print(listfunction)
