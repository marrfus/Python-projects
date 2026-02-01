position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [" "," "," "," "," "," "," "," "," "]
play= True
currentPlayer= "X"
eingabe = {"X":[],"O":[]}
counter = 0

 
def printBoard(a:list):
    """
    Druckt die ganze Board in aktueller Zustand aus.
    """
    print(rf"""        
          {a[0]} | {a[1]} | {a[2]} 
        -------------
          {a[3]} | {a[4]} | {a[5]} 
        -------------
          {a[6]} | {a[7]} | {a[8]} 
        """)  
      

def playGame(): 
    """
    Empfängt den Zug des Spielers, überprüft ihn und schreibt ihn auf die Board.
    Speichert Eingsabe und Wechselt Spieler. 
    """   
    global currentPlayer
    global eingabe
   
    while True:
        try:
            wahl = int(input(f"{currentPlayer} dran:  "))
            if 1<=wahl<=9:
                break
            else:
                raise Exception("Gib bitte Zahl von 1 bis 9!")
        except ValueError as error:
                print(f"Error: {error}")
        except Exception as e:
                print("Error: ",e) 
        
   
    while board[wahl-1] != " ":  
        try:      
            wahl = int(input(f"Leider ist Feld {wahl} schon besetzt.\nWahl bitte freie Feld:   "))
            if 1<=wahl<=9:
                break
            else:
                raise Exception("Gib bitte Zahl von 1 bis 9!")
        except ValueError as e:
                print("Keine buchstaben.Es ist einfach!!! ",e)                 
        except Exception as e:
                print("Error: ",e)  
                
    

    board[wahl-1] = currentPlayer
    eingabe[currentPlayer].append(wahl) 
    switchPlayer()

 
def switchPlayer():
    """ Spieler Wechsellung.
    """
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer="X"
 

def checkWin():
    """
    """
    global play
    global currentPlayer
    global counter 

    counter += 1
    win_liste = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    for i in win_liste:
        if all(zahl in eingabe["X"] for zahl in i):
            play = False
            print(f"Huu-hhuuu!!! Spieler X hat gewonnen!")
            break
        if all(zahl in eingabe["O"] for zahl in i):
            play = False
            print(f"Huu-hhuuu!!! Spieler O hat gewonnen!")
            break
    if counter == 9 and play == True:
        play = False
        print("Es ist Unentschieden. Ende!")

    # #oder viel einfacher das machen:
    # for i in win_liste:
    #     if board[i[0]]==board[i[1]]==board[i[2]]=="X":
    #         play = False
    #         print(f"Huu-hhuuu!!! Spieler X hat gewonnen!")
    #         break
    #     if board[i[0]]==board[i[1]]==board[i[2]]=="O":
    #         play = False
    #         print(f"Huu-hhuuu!!! Spieler O hat gewonnen!")
    #         break
        
    

print("Lass uns XO spielen!\nHier sind die mögliche Positionnen:")
printBoard(position)
while play:
    playGame()
    printBoard(board)
    # print(f"eingabe:  {eingabe}")
    checkWin()