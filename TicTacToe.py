# Mapping the TicTacToe board using dictionary.

theBoard = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ',
            'middle-left': ' ', 'middle-middle': ' ', 'middle-right': ' ',
            'bottom-left': ' ', 'bottom-middle': ' ', 'bottom-right': ' '}


def printBoard(board):
    print(board['top-left'] + '|' + board['top-middle'] + '|' + board['top-right'])
    print("-+-+-")
    print(board['middle-left'] + '|' + board['middle-middle'] + '|' + board['middle-right'])
    print("-+-+-")
    print(board['bottom-left'] + '|' + board['bottom-middle'] + '|' + board['middle-right'])

turn = "X"

for count in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on which space?")

    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
        
printBoard(theBoard)