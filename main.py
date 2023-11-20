import random

def main():
    table = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
    p1Name = input("Select player 1 name: ")
    p2Name = input("Select player 2 name: ")
    pNames = [p1Name, p2Name]
    turn = random.randint(1,2)
    #X es 1, O es 2
    playing = True

    while playing:

        if turn == 1:
            turn = 2

        else:
            turn = 1
        
        x,y = inputMove(pNames[turn-1])
        table = addPiece(x, y, turn, table)
        printTable(table)
        checkWin(table)


def inputMove(pname):
    print(f"\nTurno de {pname}!\n")

    xUser = input("Ingrese su ficha: ")
    digitList = [int(digit) for (digit) in xUser if digit.isdigit()]
    return digitList[0], digitList[1]


def addPiece(x, y, turn, table):
    if turn == 1:
        table[x-1][y-1] = "X"
        
    if turn == 2:
        table[x-1][y-1] = "O"

    return table


def printTable(table):
    print('0 1 2 3')

    for i in range(3):
        print(f"{i+1} ", end="")
        print(' '.join(table[i]))

    print("")


def checkWin(table):
    for i in range(3):

        if table[0][i] == table[1][i] == table[2][i]:

            if table[0][i] == "X":
                print("X wins!")

            elif table[0][i] == "O":
                print("O wins!")

    for i in range(3):

        if table[i][0] == table[i][1] == table[i][2]:

            if table[i][0] == "X":
                print("X wins!")

            elif table[i][0] == "O":
                print("O wins!")

    if table[0][0] == table[1][1] == table[2][2]:

        if table[1][1] == "X":
            print("X wins!")
            
        elif table[1][1] == "O":
            print("O wins!")

    if table[2][0] == table[1][1] == table[0][2]:

        if table[1][1] == "X":
            print("X wins!")

        elif table[1][1] == "O":
            print("O wins!")


main()
