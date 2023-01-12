ManiMartas = 10
firstgamemachne = 1
firstgamemachne2 = 0
plays = 0

while ManiMartas > 0:
    if firstgamemachne !=3 or firstgamemachne2 !=4:
        while firstgamemachne < 3 and ManiMartas > 0:
            firstgamemachne += 1
            plays += 1
            ManiMartas -= 1
            print('lose x 1', firstgamemachne, ManiMartas)
            while firstgamemachne2 < 4 and ManiMartas > 0:
                firstgamemachne2+=1
                plays += 1
                ManiMartas -= 2
                print('lose x 2', firstgamemachne2, ManiMartas)
                break
    if firstgamemachne >= 3 or firstgamemachne2 >= 4:
        while firstgamemachne >= 3:
            firstgamemachne = 0
            ManiMartas += 2
            print("win", firstgamemachne, ManiMartas)
            while firstgamemachne2 >= 4:
                firstgamemachne2 = 0
                ManiMartas += 7

                print('win x 2', firstgamemachne2, ManiMartas)


if ManiMartas >= 0:
    print("вы банкрот")
print(f"Общий итог денег {ManiMartas}, количество игр {plays}")


