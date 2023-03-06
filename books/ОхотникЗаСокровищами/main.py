import random
import sys
import math

def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = ' '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()
    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ' '
        boardRow= ''
        for column in range(60):
            boardRow += board[column][row]
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
            smallestDistance = distance
    smallestDistance = round(smallestDistance)
    if smallestDistance == 0:
        chests.remove([x, y])
        return 'Вы нашли сундук с сокровищами на затонувшем судне'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости.'
        else:
            board[x][y] = 'X'
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне зоны досягаемости.'

def enterPlayerMove(previousMoves):
    print('Где следует опустить гидролокатор? (координата: 0-59 0-14)(или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру!')
            sys.exit()
            move = move.split()
            if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and \
            isOnBoard(int(move[0]), int(move[1])):
                if [int(move[0]), int(move[1])] in previousMoves:
                    print('здесь вы уже опускали гидролокатор.')
                    continue
                return [int(move[0]), int(move[1])]
            print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14')

def showInstructions():
    print('''Инструктаж:
    Вы капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
    --пропуск-- 
   
    Нажмите не клавишу Enter, чтобы продолжить...''')
    input()

print('Охотник за сокровищами')
print()
print('Показать инструкции (да/нет)')
if input().lower().startswith('д'):
    showInstructions()
previousMoves = []
while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    while sonarDevices > 0:
        print('Осталось гидролокаторовН: %s. Осталось сундуков с сокровищами:%s.' % (sonarDevices, len(theChests)))
        x, y = enterPlayerMove(previousMoves)
        previosMoves.append([x, y])
    moveResult = makeMove(theBoard, theChrsts, x, y)
    if moveResult == False:
        dontinue
    else:
        if moveResult == 'Вы нашли сундук с сокровищами на затонувшем судне!':
            for x, y in previousMoves:
                makeMove(theBoard, theChests, x, y)
                drawBoard(theBoard)
                print(moveResult)
        if len(theChests) == 0:
            print('Вы нашли все сундуки с сокровищами на затонувших суднах! Поздравляем и приятной игры!')
            break
        sonarDevices -= 1
    if sonarDevices == 0:
        print('Все гидролокаторы опущены на дно! Придется разворачивать корабль м')
        print('отправляться домой, в порт! Игра окончена.')
        print('Вы не нашли сундукм в следующих местах:')
        for x, y in theChests:
            print(' %s, %s' % (x, y))
        print('Хотите сыграть еще раз? (да или нет)')
        if not input().lower().startswith('д'):
            sys.exit()
