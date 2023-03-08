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

    if title == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while inOnBoard (x, y) and  board[x][y] == otherTile:

            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == title:

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

def getBoardWithValidMoves(board, title):

    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, title):
        boardCopy[x][y] = '.'
    return  boardCopy

def getValidMoves(board, title):

    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, title, x, y) != False:
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

def enterPlayerTitle():


    title = ''
    while not (title == 'X' or title == 'O'):
        print('Вы играете за Х или О?')
        title = input().upper()


        if tile == 'X':
            return  ('X', 'O')
        else:
            return ('O', 'X')

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board, title, xstart, ystart):


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

def getPlayerMove(board, playerTitle):


        DIGITSITO8 = '1 2 3 4 5 6 7 8'.split()
        while True:
            print('Укажите код, текст "выход" для завершения или "подсказка" для вывода подсказки')
            move = input().lower()
            if move == 'выход' or move == 'подсказка':
                return move

            if len(move) == 2 and move[0] in DIGITSITO8 and move[1] in DIGITSITO8:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if isValidMove(board, playerTitle, x, y) == False:
                    continue
                else:
                    break













































































