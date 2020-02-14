import random


text = str(input("Enter your name: "))

def Namekey(a, b, c):
     key = {a: random.randint(b, c)}
     return key

print (Namekey(text, 0, 50))