'''
Бинарный поиск
'''



def binary2(A, key):
    Attempt = 0
    left = -1
    right = len(A)
    key = int(key)
    GG = 0
    while GG != 1:
        middle = (left + right) // 2
        B = int(A[middle])
        if B > key:
            right = middle
            Attempt += 1
            print(right)
            print("Теплее")
        elif B < key:
            left = middle
            print(left)
            Attempt += 1
            print("Холодно")
        elif B == key:
            print(f"Ваше число {B}")
            GG += 1
        else:
            print("Что-то пошло не так!!!")

    return f'Число попыток чтобы угадать {Attempt}!!'



if __name__ == "__main__":
    print("А теперь 2 способом")
    print("Введите число от 0 до 99 а программа угадает")
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myitem = 7

    print(binary2(mylist, myitem))