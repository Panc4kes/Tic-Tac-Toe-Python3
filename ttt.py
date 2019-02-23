import sys
pos = {
    "1":{"1": " ", "2": " ", "3": " ",},
    "2":{"1": " ", "2": " ", "3": " ",},
    "3":{"1": " ", "2": " ", "3": " ",}
    }

def test():
    comb = [pos["1"]["1"]+pos["1"]["2"]+pos["1"]["3"],
       pos["2"]["1"]+pos["2"]["2"]+pos["2"]["3"],
       pos["3"]["1"]+pos["3"]["2"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["1"]+pos["3"]["1"],
       pos["1"]["2"]+pos["2"]["2"]+pos["3"]["2"],
       pos["1"]["3"]+pos["2"]["3"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["2"]+pos["3"]["3"],
       pos["3"]["1"]+pos["2"]["2"]+pos["1"]["3"]]

    if "OOO" in comb:
        print("PLAYER 1 WON!")
        ask()
    elif "XXX" in comb:
        print("PLAYER 2 WON!")
        ask()

def display():
    print("[{0}][{1}][{2}]".format(pos["1"]["1"],pos["2"]["1"],pos["3"]["1"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["2"],pos["2"]["2"],pos["3"]["2"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["3"],pos["2"]["3"],pos["3"]["3"]))

def resolve(posi,turn):
    try:
        x,y = eval(posi)
    except:
        print("Invalid coordinates, try again!")
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
            pos[str(x)][str(y)] = sym
            display()
    except:
        print("coordinates outside of range! (max 3,3)")
        if turn == "X":
                P2()
        else:
                P1()


def P1():
    test()
    turn = "O"
    print("give coordinates of placement, x,y.")
    print("Player 1's turn!")
    resolve(input(),turn)
    P2()

def P2():
    test()
    turn = "X"
    print("give coordinates of placement, x,y.")
    print("Player 2's turn!")
    resolve(input(),turn)
    P1()

def ask():
    print("play again? Y/N")
    inp = input()
    if inp.lower() == "y":
        P1()
    elif inp.lower() == "n":
        sys.exit()
    else:
        print("Undefined keyword")
        ask()
P1()
