list1 = [10]
list1.append(20)
print(list1)
list1.append(30)
print(list1)
list2 = [40, 50]
list2.append(60)
list1.extend(list2)
list1.insert(1, 15)
print(list1)
list1.sort(reverse=True)
print(list1)
list3 = list1.pop(0)
print(list1, list3)

print('Размер деревни, Village a size/ Ввести количество деревень, Enter the number of villages')
n = int(input()) # 5
position = []
for i in range(n): # 5
    print('Введите по очереди размеры каждой деревни/Enter the sizes of each village in turn')
    position.append(int(input())) # 5 чисел  1 3 5 7 9

position.sort() # Сортировочка
left = (position[1] - position[0]) / 2  # позиция 0 тут 1 поз 1 3 3-1=2\2=1
right = (position[2] - position[1]) / 2 # 5 - 3 = 2==1
min_size = left + right

for i in range(2, n - 1):  #Рандж начинается с 0 1 2   количество деревень - 1 не учитывать последний
    print('я тут ай', i, 'я тут н', n)
    left2 = (position[i] - position[i - 1])/2  # 5 - 5э\2
    right2 = (position[i + 1] - position[i])/2

    size = left2 + right2
    print(size, n)
    if size < min_size:
        min_size = size
print('Минитальный размер соседних деревень')
print(min_size)






