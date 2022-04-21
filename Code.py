# tick tac toe AI based

import sys
import random

# creating a dictionary
board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', }


# for printing the board
def displayboard(board):
    print('\n')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + '    1 | 2 | 3')
    print('- + - + -' + '    - + - + -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + '    4 | 5 | 6')
    print('- + - + -' + '    - + - + -')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + '    7 | 8 | 9')
    print("\n")


# to check if there is a place to input in the board
def space_available(position):
    if board[position] == ' ':
        # ' ' represents empty space if space empty found then only input will be taken
        return True
    else:
        return False


def checkdraw():
    # if there is no empty space left and no one wins, we declace the game as DRAW
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True


def checkwin():
    # checking in Row level
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    # checking in Diagonal level
    elif board[1] == board[5] == board[9] and board[5] != ' ':
        return True
    elif board[3] == board[5] == board[7] and board[3] != ' ':
        return True
    # checking in Column level
    elif board[1] == board[4] == board[7] and board[4] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[9] != ' ':
        return True
    else:
        return False


def checkwhowon(mark):
    if board[1] == board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] == board[9] and board[7] == mark:
        return True
    # checking in Diagonal level
    elif board[1] == board[5] == board[9] and board[5] == mark:
        return True
    elif board[3] == board[5] == board[7] and board[3] == mark:
        return True
    # checking in Column level
    elif board[1] == board[4] == board[7] and board[4] == mark:
        return True
    elif board[2] == board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] == board[9] and board[9] == mark:
        return True
    else:
        return False


def inserting(symbol, position):
    if space_available(position):
        board[position] = symbol
        displayboard(board)
        if checkdraw():
            print("Draw")
            sys.exit()

        if checkwin():
            if symbol == 'X':
                print("Bot win")
                sys.exit()

            else:
                print("Player win")
                sys.exit()


    else:
        print("invalid input")
        position = int(input("Enter new position :"))
        inserting(symbol, position)
        return


# declaring globaly symbol for player and computer
player = 'O'
bot = 'X'


# for taking input from user/ Player
def player_move():
    position = int(input("Enter position for O :"))
    inserting(player, position)
    return


def computer_move():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    inserting(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if checkwhowon(bot):
        return 1
    elif checkwhowon(player):
        return -1
    elif checkdraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def firstpick():
    randomchance = [0, 1]
    checkfirst = random.choice(randomchance)

    if checkfirst == 0:
        print("Bot first -- ")
        while (checkwin() == False and checkdraw() == False):
            computer_move()
            player_move()

    if checkfirst == 1:
        print("Player first -- ")
        while (checkwin() == False and checkdraw() == False):
            player_move()
            computer_move()


displayboard(board)
firstpick()




