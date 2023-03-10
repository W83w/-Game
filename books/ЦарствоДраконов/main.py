import random
import time

def displayIntro():
    print('''
    Вы находитесь в землях, заселенные драконами. 
    Перед собой вы видите две пещеры. В одной из них голодный дракон. 
    ''')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите 1 или 2)')
        cave = input()

    return cave

def chackCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2) # использовал в первый раз, чтобы подождать 2 секунды для интриги

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('.. отпускает! Он вы успели что то уточить у дракона')
    else:
        print('..моментально съедает')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    chackCave(caveNumber)

    print('Попытать удачу еще раз?(да или нет)')
    playAgain = input()