import os
def WelcomeBanner():
    print("X O X O X O X O X O X O X O X O X")
    print("O                               X")
    print("X     Noughts and Crosses       O")
    print("O                               X")
    print("X O X O X O X O X O X O X O X O X")
    print(" ")

gameRunning = True
selectPlayer = "X"
winner = None
x = 0
y = 0
z = 0

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def displayBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print(" ")
    print("-----------------------------------------------")
    print(" ")

def menu():
    print("1. Play game")
    print("2. View game history")
    print("3. Exit")
    inputMain = int(input("Enter your choice: "))
    if (inputMain == 1 ):
        main()
    elif(inputMain == 2):
        view_game_history()
        return menu()
    elif (inputMain == 3):
        exit()
        
def playerInput(board):
    print(f"Player {selectPlayer} : Your Turn!!")
    inp = int(input("Enter a 1-9 position number to put an x in? or Quit Game(Enter '0'): "))
    if (inp>=1 and inp<=9 and board[inp-1]=="-"):
        board[inp-1]=selectPlayer
    elif(inp == 0):
        print("Game Over..")
        save_game_stats()
        resetBoard()
        return menu()
    else:
        print("Sorry this position is already taken... Try again!")
        return playerInput(board)

def checkBoard(board):
    #Checking the first row...
    global winner
    if board[0]=="X" and board[1]=="X" and board[2]=="X":
        print("Three Xs in a row.")
        winner = board[0]
        return True
    elif board[0]=="O" and board[1]=="O" and board[2]=="O":
        print("Three Os in a row.")
        winner = board[0]
        return True
        
    #Checking the second row...
    if board[3]=="X" and board[4]=="X" and board[5]=="X":
        print("Three Xs in a row.")
        winner = board[3]
        return True
        
    elif board[3]=="O" and board[4]=="O" and board[5]=="O":
        print("Three Os in a row.")
        winner = board[3]
        return True
        
    #Checking the third row...
    if board[6]=="X" and board[7]=="X" and board[8]=="X":
        print("Three Xs in a row.")
        winner = board[6]
        return True
        
    elif board[6]=="O" and board[7]=="O" and board[8]=="O":
        print("Three Os in a row.")
        winner = board[6]
        return True
        

    #Checking the first column
    if board[0]=="X" and board[3]=="X" and board[6]=="X":
        print("Three Xs in a column.")
        winner = board[0]
        return True
        
    elif board[0]=="O" and board[3]=="O" and board[6]=="O":
        print("Three Os in a column.")
        winner = board[0]
        return True
        
    #Checking the second column 
    if board[1]=="X" and board[4]=="X" and board[7]=="X":
        print("Three Xs in a column.")
        winner = board[1]
        return True
        
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
        print("Three Os in a column.")
        winner = board[1]
        return True

    #Checking the third column
    if board[2]=="X" and board[5]=="X" and board[8]=="X":
        print("Three Xs in a column.")
        winner = board[2]
        return True

    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
        print("Three Os in a column.")
        winner = board[2]
        return True

    #Checking the first diagonale
    if board[0]=="X" and board[4]=="X" and board[8]=="X":
        print("Three Xs in a diagonale.")
        winner = board[0]
        return True
        
    elif board[0]=="O" and board[4]=="O" and board[8]=="O":
        print("Three Os in a diagonale.")
        winner = board[0]
        return True

    #Checking the second diagonale
    if board[2]=="X" and board[4]=="X" and board[6]=="X":
        print("Three Xs in a diagonale.")
        winner = board[2]
        return True
        
    elif board[2]=="O" and board[4]=="O" and board[6]=="O":
        print("Three Os in a diagonale.")
        winner = board[2]
        return True
def checkTie(board):
    global gameRunning
    global winner
    if "-" not in board:
        print("It is a tie...")
        counts()
        resetBoard()
        winner = None
        inp1 = str(input("Do you want to continue this game(y/n): "))
        if (inp1 == "y"):
            resetBoard()
            gameRunning = True
        elif (inp1 == "n"):
            save_game_stats()
            resetBoard()
            return menu()

def checkWinner(): 
    global board
    global gameRunning
    global winner
    if checkBoard(board):
        print(f"Game Over!! The winner is Player {winner}")
        counts()
        winner = None
        inp1 = str(input("Do you want to continue this game(y/n): "))
        if (inp1 == "y"):
            resetBoard()
            gameRunning = True
        elif (inp1 == "n"):
            save_game_stats()
            resetBoard()
            return menu()


def switchPlayer():
    global selectPlayer
    if selectPlayer == "X":
        selectPlayer = "O"
    else:
        selectPlayer ="X"

def save_game_stats():
    if not os.path.exists("game_history"):
        os.makedirs("game_history")
    session_file = os.path.join("game_history", f"session_{len(os.listdir('game_history')) + 1}.txt")
    with open(session_file, "w") as file:
        file.write(f"Player X wins: {x} \n")
        file.write(f"Player O wins: {y} \n")
        file.write(f"Draws: {z} \n")

def view_game_history():
    if not os.path.exists("game_history"):
        print("No game history found.")
        return
    for filename in os.listdir("game_history"):
        with open(os.path.join("game_history", filename), "r") as file:
            print(f"Session {filename.split('_')[1].split('.')[0]}")
            print(file.read())
def counts():
    global x
    global y
    global z
  
    if (winner == "X"):
        x += 1
    elif (winner == "O"): 
        y += 1
    elif(winner == None):
        z += 1

def resetBoard():
    global board
    board = ["-","-","-",
            "-","-","-",
            "-","-","-",]

def main():
    global gameRunning
    while True:
        WelcomeBanner()
        playerInput(board)
        displayBoard(board)
        checkTie(board)
        switchPlayer()
        checkWinner()

while gameRunning:
    menu()