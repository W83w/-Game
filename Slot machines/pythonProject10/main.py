ManiMartas = 5
firstgamemachne = 1
firstgamemachne2 = 0
dygame = 0
while firstgamemachne < 3 and ManiMartas > 0:
    firstgamemachne += 1
    ManiMartas -= 1
    print("Деньги и игры", ManiMartas, firstgamemachne)

    while firstgamemachne >= 3 and ManiMartas > 0:
        firstgamemachne = 0
        ManiMartas += 2
        print("Win Деньги и игры", ManiMartas, firstgamemachne)
        while firstgamemachne2 <4 and ManiMartas > 0:
            firstgamemachne2 += 1
            ManiMartas -= 2
            print("Деньги и игры", ManiMartas, firstgamemachne2 )
            while firstgamemachne2 >= 4 and ManiMartas > 0:
                firstgamemachne2 = 0
                ManiMartas += 7
                print('Win на 2 автомате', ManiMartas, firstgamemachne2)
if ManiMartas >= 0:
    print("вы банкрот")
print("Общий итог денег", ManiMartas)
print(firstgamemachne)

