ManiMartas = 4
firstgamemachne = 1
firstgamemachne2 = 0
dygame = 0
while firstgamemachne < 3 and ManiMartas > 0:
    firstgamemachne += 1
    ManiMartas -= 1
    print("Деньги и игры", ManiMartas, firstgamemachne)
    while firstgamemachne >= 3:
        firstgamemachne = 0
        ManiMartas += 2
        print("Win Деньги и игры", ManiMartas, firstgamemachne)
if ManiMartas >= 0:
    print("вы банкрот")
print("Общий итог денег", ManiMartas)
print('', firstgamemachne)
