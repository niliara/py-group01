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
        #table = addPiece(x, y, turn, table)
        printTable(table)
        #checkWin(table)

def inputMove(pname):
    print(f"\nTurno de {pname}!\n")

    xUser = input("Ingrese su ficha: ")
    digitList = [int(digit) for (digit) in xUser if digit.isdigit()]
    return digitList[0], digitList[1]

def addPiece(x, y, turn, table):
    #CAMBIA EL VALOR DE UNA POSICION AL DEL TURNO
    #CAMBIA TURNO
    #COMPRUEBA SI HA GANADO
    pass

def printTable(table):
    print('0 1 2 3')
    for i in range(3):
        print(f"{i+1} ", end="")
        print(' '.join(table[i]))
    print("")

def checkWin(table):
    pass




main()
