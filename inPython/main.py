#tic tac toe board
board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

#printing the board to the console
def displayBoard():

    for i in range(0,3):

        for j in range(0,3):

            print(board[i][j], end=" ")
        
        print("\n")

#turn count
turn = 0

def changeUser():
    
    if turn % 2 == 0:
    
        return "X"
    
    else:
    
        return "O"


def coordinates(userInput):
    global row
    row = int(userInput / 3)
    global col 
    col = userInput
    if col > 2: 
        col = int(col %3)
    return (row, col)


def isTaken(slot):

    coordinates(slot)

    if board[row][col] != '-':
        
        return False
    
    else:
        
        return True


def checkInput(userInput):

    check = True

    if type(userInput) != int:
        
        check = False

        return "not a number"
    
    elif userInput > 1 or userInput < 9:
        
        check = False

        return "out of bounds"
    
    else:

        return "valid input"
    
