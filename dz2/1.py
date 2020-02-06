import random
list= []
for l in range(10):
    l= int(random.randint(1,10))
    list.append(l)

print(list)
list.pop()
print(list)