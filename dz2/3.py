import random

a = int(random.randint(0,10))
b = int(random.randint(0,10))
c = int(random.randint(0,10))
print(a)
print(b)

if a == b:
    print(c, "Теперь эта")
    if c < a+b:
        print("Сегодня понедельник")
    else:
        print("Сегодня будет торт")

if c == a+b:
    print("Страдания")
else:
    if a > b:
        print("Доброе утро!")
    else:
         print("Горите в аду")
