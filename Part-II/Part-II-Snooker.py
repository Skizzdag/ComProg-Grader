#Part-II-Snooker
P1 = 0
P2 = 0
Color = {"X":0,"R":1,"Y":2,"G":3,"W":4,"B":5,"P":6,"K":7}
while True:
    inp = input()
    if len(inp) == 3:
        if inp[0] == "1":
            P1 += Color[inp[1]]+Color[inp[2]]
        elif inp[0] == "2":
            P2 += Color[inp[1]]+Color[inp[2]]
    elif len(inp) == 2:
        if inp[0] == "1":
            P1 += Color[inp[1]]
        elif inp[0] == "2":
            P2 += Color[inp[1]]
    if len(inp) == 2 and inp[1] == "K":
        break
if P1 == P2:
    print(P1,P2)
    print("Tie")
elif P1>P2:
    print(P1,P2)
    print("Player 1 wins")
elif P1<P2:
    print(P1,P2)
    print("Player 2 wins")