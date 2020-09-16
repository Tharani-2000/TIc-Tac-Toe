# The game space
# Ignoring 0 index and having game board space = 9

board = [" " for i in range(10)]
pos_board = [str(i) for i in range(10)]


# Whether the pos is currently available
def isfree(position):
    return board[position] == ' '


# print the board
def printboard(bo=board):
    print()
    print(' ' + bo[1] + ' | ' + bo[2] + ' | ' + bo[3])
    print('-----------')

    print(' ' + bo[4] + ' | ' + bo[5] + ' | ' + bo[6])
    print('-----------')

    print(' ' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])
    print()


def iswinner(board, player):
    return ((board[7] == player and board[8] == player and board[9] == player) or  # across the top
            (board[4] == player and board[5] == player and board[6] == player) or  # across the middle
            (board[1] == player and board[2] == player and board[3] == player) or  # across the bottom
            (board[7] == player and board[4] == player and board[1] == player) or  # down the left side
            (board[8] == player and board[5] == player and board[2] == player) or  # down the middle
            (board[9] == player and board[6] == player and board[3] == player) or  # down the right side
            (board[7] == player and board[5] == player and board[3] == player) or  # sec-diagonal
            (board[9] == player and board[5] == player and board[1] == player))  # diagonal


def isfull():
    return not board.count(" ") > 1


def insert(letter, pos):
    board[pos] = letter


def playmove():
    run = True

    while run:
        move = input(" Please select a position to place an \'X\' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:  # makes sure we type in a number between 1-9
                if isfree(move):  # check if the move we choose is valid (no other letter is there already)
                    run = False
                    insert('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compmove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if iswinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


print("Welcome to Tic Tac Toe")


def main():
    printboard(pos_board)

    while True:
        while not isfull():
            if not iswinner(board, "O"):
                playmove()
                printboard()
            else:
                print("Computer won the game!!!!!!!!!")
                return

            if not iswinner(board, "X"):
                if isfull():
                    return
                else:
                    move = compmove()
                    insert("O", move)
                    print('Computer placed an \'O\' in position', move, ':')
                    printboard()
            else:
                print("You won the game!!!!!!!!!")
                return

        if isfull():
            print("TIE GAME!!!")
            return


main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        for i in range(len(board)):
            board[i] = " "
        print('-----------------------------------')
        main()
    else:
        break
