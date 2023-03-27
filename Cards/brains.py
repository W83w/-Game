import random
def Brain():
    deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(deck)
    count = 0
    while True:
        choice = input('Будете брать карту?').lower()
        if choice in 'yes' or choice in 'да':
            current = deck.pop()
            print(f'Вам попалась карта достоинства {current}')
            count += current
            if count > 21:
                print('Извините но вы проиграли!!!')
                break
            elif count == 21:
                print('Поздравляем, вы набрали 21')
                break
            else:
                print(f'У вас {count} очка')
        elif choice in 'no' or choice in 'нет':
            print(f'У вас {count} очков и вы закончили игру.')
            break

    print("Спасибо за игру!!!!. До новых встреч!")