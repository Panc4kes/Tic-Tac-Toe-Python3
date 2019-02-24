import sys, platform, os

global pos

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

__license__ = open("LICENSE","r").read()

allTurns = 0

pos = {
    "1":{"1": " ", "2": " ", "3": " ",},
    "2":{"1": " ", "2": " ", "3": " ",},
    "3":{"1": " ", "2": " ", "3": " ",}
    }

def menu():
    clear()
    print("="*30)
    print("= "+"Welcome to Tic Tac Toe!".center(26)+" =")
    print("="*30+"\n")
    print("select an option below")
    print("1 = Player vs Player")
    print("2 = License")
    print("3 = Exit")
    inp = input("> ")

    if inp == "1":
        clear()
        P1()
    elif inp == "2":
        clear()
        print(__license__)
        print("\nPress 'enter' to return to menu")
        input()
        menu()
    elif inp == "3":
        sys.exit()
    else:
        print("Invalid keyword, press 'enter' to return to menu\n")
        input()
        menu()

def test():
    global pos
    global comb
    comb = [pos["1"]["1"]+pos["1"]["2"]+pos["1"]["3"],
       pos["2"]["1"]+pos["2"]["2"]+pos["2"]["3"],
       pos["3"]["1"]+pos["3"]["2"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["1"]+pos["3"]["1"],
       pos["1"]["2"]+pos["2"]["2"]+pos["3"]["2"],
       pos["1"]["3"]+pos["2"]["3"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["2"]+pos["3"]["3"],
       pos["3"]["1"]+pos["2"]["2"]+pos["1"]["3"]]

    if "OOO" in comb:
        print("GAME OVER: PLAYER 1 WON!")
        ask()
    elif "XXX" in comb:
        print("GAME OVER: PLAYER 2 WON!")
        ask()
    elif allTurns == 9:
        print("GAME OVER: TIE")
        ask()

def display():
    print("\n[{0}][{1}][{2}]".format(pos["1"]["1"],pos["2"]["1"],pos["3"]["1"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["2"],pos["2"]["2"],pos["3"]["2"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["3"],pos["2"]["3"],pos["3"]["3"]),"\n")

def resolve(posi,turn):
    global allTurns
    try:
        x,y = eval(posi)
    except:
        print("Invalid coordinates, try again!\n")
        if turn == "X":
            P2()
        else:
            P1()
    sym = turn
    try:
        if pos[str(x)][str(y)] in ["X","O"]:
            print("There's already a marker there!")
            display()
            if turn == "X":
                P2()
            else:
                P1()
        else:
            allTurns += 1
            pos[str(x)][str(y)] = sym
            display()
    except:
        print("Coordinates outside of range! (max 3,3)\n")
        if turn == "X":
            P2()
        else:
            P1()


def P1():
    test()
    turn = "O"
    print("Give coordinates of placement, in the format of x,y")
    print("Player 1's turn!\n")
    resolve(input("> "),turn)
    P2()

def P2():
    test()
    turn = "X"
    print("Give coordinates of placement, in the format of x,y")
    print("Player 2's turn!\n")
    resolve(input("> "),turn)
    P1()

def exit():
    sys.exit()
    
def ask():
    global pos
    global allTurns
    global comb
    while True:
        print("\nplay again? (Y/N)")
        inp = input("> ")
        if inp.lower() == "n":
            exit()
            
        elif inp.lower() == "y":
            pos = {
    "1":{"1": " ", "2": " ", "3": " ",},
    "2":{"1": " ", "2": " ", "3": " ",},
    "3":{"1": " ", "2": " ", "3": " ",}
    }
            allTurns = 0
            clear()
            P1()
        else:
            print("Undefined keyword")

menu()
