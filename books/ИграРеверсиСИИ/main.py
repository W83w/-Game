# 'Реверси'
import random
import sys
WIDTH = 8 # игровое поле содержит 8 клеток по ширине
HEIGHT = 8 # 8 клеток по высоте
def drawBoard(board):

    print(' 12345678')
    print("+--------+")
    for y in range(HEIGHT):
        print(f"{y + 1}", end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y + 1))
    print("+--------+")
    print(' 12345678')

def getNewBoard():

    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):


    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard (x, y) and  board[x][y] == otherTile:

            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:

                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x, y):

    return x>=0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):

    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):

    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):

    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return (f"'X':{xscore}, 'O':{oscore}") #

def enterPlayerTile():


    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Вы играете за Х или О?')
        tile = input().upper()


    if tile == 'X':
        return  ('X', 'O')
    else:
        return ('O', 'X')

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board, tile, xstart, ystart):


    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):

    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy

def isOnCorner(x, y):

    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getPlayerMove(board, playerTile):


    DIGITSITO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Укажите код, текст "выход" для завершения или "подсказка" для вывода подсказки')
        move = input().lower()
        if move == 'выход' or move == 'подсказка':
            return move

        if len(move) == 2 and move[0] in DIGITSITO8 and move[1] in DIGITSITO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Это недопустимый ход. Введите номер столбца (1 - 8) и номер ряда (1 - 8).')
            print('К примеру, значение 81 перемешает в верхний правый угол.')

    return [x, y]

def getComputerMove(board, computerTile):


    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)


    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]


    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('Ваш счет: %s. Счет компьютера: %s.' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print(turn + ' ходит первым.')


    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == 'Человек':
            if playerValidMoves != []:
                if showBints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'выход':
                    print('Спасибо за игру!')
                    sys.exit()
                elif move == 'подсказка':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'Компьютер'

        elif turn == 'Компьютер':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Нажмите клавишу Enter для просмотра хода компьютера.')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'Человек'



print('Приветствуем в игре "Реверси" !')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X набрал %s очков. O набрал %s очков.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('Вы победили компьютер, обыграв его на %s очков! Поздравляем!' % (scores[computerTile] - \
        scores[playerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('Вы проиграли. Компьютер обыграл человечество на %s очков.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('Ничья! У человечества есть шанс')

    print('Хотите сыграть еще раз? (да нет)')
    if not input().lower().startswith('д'):
        break






































































