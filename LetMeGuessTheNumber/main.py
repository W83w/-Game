from Sort import binary
from Sort1 import binary2

mylist = []

for i in range(100):
    mylist.append(i)

print("Введите число от 0 до 99 а программа угадает")
myitem = input()

print(binary(mylist, myitem))


print("А теперь 2 способом")
print("Введите число от 0 до 99 а программа угадает")
myitem = input()

print(binary2(mylist, myitem))

