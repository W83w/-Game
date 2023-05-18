'''
Линейный поиск в массиве
'''

mylist = []

for i in range(100):
    mylist.append(i)



def binary(list, item):
    low = 0
    high = len(list)-1
    Attempt = 0

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        guess = int(guess)

        item = int(item)
        if guess == item:
            print("Угадал")
            print(f"Попыток что бы угадать {Attempt}!!")
            return mid

        if guess > item:
            print("Тепло")
            Attempt += 1
            high = mid - 1

        else:
            print("Холодно")
            low = mid + 1
            Attempt += 1
    return None


if __name__ == "__main__":
    print("А теперь 2 способом")
    print("Введите число от 0 до 99 а программа угадает")
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myitem = 7

    print(binary(mylist, myitem))

