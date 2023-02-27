# Крестики нолики

import random

def drawBoard(board):



    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():


    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O')
        letter = input().upper()


        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(border, letter, move):
    border[move] = letter

def isWinner(bo, le):


    return((bo[7] == le and bo[8] == le and bo[9] == le) or
           (bo[4] == le and bo[5] == le and bo[6] == le) or
           (bo[1] == le and bo[2] == le and bo[3] == le) or
           (bo[7] == le and bo[4] == le and bo[1] == le) or
           (bo[8] == le and bo[5] == le and bo[2] == le) or
           (bo[9] == le and bo[6] == le and bo[3] == le) or
           (bo[7] == le and bo[5] == le and bo[3] == le) or
           (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):

    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):

    return board[move] == ' '

def getPlayerMove(board):

    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'



    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i


    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i


    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move


    if isSpaceFree(board, 5):
        return 5


    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoaedFull(board):

    for i in  range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

while True:

    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
#    print('', + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':

            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли!')
                gameIsPlaying = False
            else:
                if isBoaedFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'

        else:

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли!')
                gameIsPlaying = False
            else:
                if isBoaedFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз?(да нет)')
    if not input().lower().startswith('д'):
        break