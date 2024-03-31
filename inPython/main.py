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
    
    elif userInput < 1 or userInput > 9:
        
        check = False

        return "out of bounds"
    
    elif quit(userInput):
        
        check = False

        return "User Quit"
    
    elif isTaken(userInput):

        check = False

        return "Taken"

    else:

        return "valid input"
    
def replaceOnBoard(userInput, symbol):

    coordinates(userInput)

    board[row][col] = symbol
    

def Horizontal(symbol):
    
    totalCheck = True

    for i in range(0,3):
    
        for j in range(0,3):

            if board[i][j] != symbol:

                totalCheck = False
            
            else:
                
                totalCheck = True

    if totalCheck == True:
        
        return True
    
    else:

        return False


def vertical(symbol):

    totalCheck = True

    for i in range(0,3):
        
        for j in range(0,3):

            if board[j][i] != symbol:

                totalCheck = False

            else:

                totalCheck = True
    
    if totalCheck == True:

        return True
    
    else:

        return False

def diagonal(symbol):

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        
        return True
    
    elif board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:

        return True

    else:

        return False
    
def checkWin(symbol):

    if Horizontal(symbol) == True or vertical(symbol) == True or diagonal(symbol) == True:

        return True
    
    else:

        return False
    
def quit(userInput):

    if type(userInput) == str:

        if userInput.lower() == "q":

            return True
    
        else:

            return False
    
    else: 
        
        return False

#turn count
turn = 0
    
while turn <= 9:

    player = changeUser()

    displayBoard()

    position = int(input("Please input a number 1-9 to play, and enter q to quit \n"))

    numCheck = checkInput(position)

    if numCheck == "User Quit":

        break

    elif numCheck == "not a number":

        print("The input was not a number ", end = "")

        position = int(input("Please input a number 1-9 to play, and enter q to quit \n"))

        continue

    elif numCheck == "out of bounds":

        print(f"the number {position} is out of bounds ", end="")

        position = int(input("Please input a number 1-9 to play, and enter q to quit \n"))

        continue

    elif numCheck == "Taken":

        print("The slot is already taken ", end = "")

        position = int(input("PLease enter a number between 1-9 to play \n"))

        continue

    position = position - 1 #for the index

    replaceOnBoard(position, player)

    if checkWin(player):

        displayBoard()

        print(f"{player} has won!!")

        break

    turn = turn + 1

    if turn > 9:

        print("It is a tie")    

        break