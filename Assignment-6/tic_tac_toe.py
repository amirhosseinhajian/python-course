import pyfiglet
from random import randint
from colorama import Fore
from time import time

def print_game_board():
    for row in game_board:
        for cell in row:
            if cell == 'X':
                print(Fore.RED, cell, end=" ")
            elif cell == 'O':
                print(Fore.BLUE, cell, end=" ")
            else:
                print(Fore.WHITE, cell, end=" ")
        print(Fore.WHITE)
    print("************")

def check_game():
    if "X" == game_board[0][0] == game_board[1][1] == game_board[2][2] or "X" == game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return "player 1"
    elif "O" == game_board[0][0] == game_board[1][1] == game_board[2][2] or "O" == game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return "player 2"
    for i in range(3):
        if "X" == game_board[i][0] == game_board[i][1] == game_board[i][2] or "X" == game_board[0][i] == game_board[1][i] == game_board[2][i]:
            return "player 1"
        elif "O" == game_board[i][0] == game_board[i][1] == game_board[i][2] or "O" == game_board[0][i] == game_board[1][i] == game_board[2][i]:
            return "player 2"
    for row in  game_board:
        if "-" in row:
            break
    else:
        return "draw"
    return "no winner"

def game_state(state):
    if state != "no winner":
        if state == "draw":
            print("draw!")
        elif state == "player 2":
            print(f"{'pc' if game_player == 1 else 'player 2'} wins!")
        else:
            print("player 1 wins!")
        print("--- %s seconds ---" % (time() - start_time))
        exit()

title = pyfiglet.figlet_format("Tic Tac Toe")
print(title)
game_player = int(input("if you want to play with pc enter 1 and if you want to play with player 2 enter 2: "))
game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"],]
print_game_board()
while True:
    start_time = time()
    print("Player 1")
    while True:
        row = int(input("row: "))
        col = int(input("col: "))
        if row >=0 and row <= 2 and col >=0 and col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = 'X'
                break
            else:
                print("This place is taken")
        else:
            print("index out of range")
    print_game_board()
    game_state(check_game())
    if game_player == 2:
        print("Player 2")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if row >=0 and row <= 2 and col >=0 and col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = 'O'
                    break
                else:
                    print("This place is taken")
            else:
                print("index out of range")
    else:
        row = randint(0, 2)
        col = randint(0, 2)
        while game_board[row][col] != '-':
            row = randint(0, 2)
            col = randint(0, 2)
        game_board[row][col] = 'O'
    print_game_board()
    game_state(check_game())
