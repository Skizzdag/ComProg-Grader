#Part-I-Rock-Scissor-Paper
m = int(input())
S1,S2 = 0,0
k = 0
while True:
    P1,P2 = input().split()
    if P1 == "R":
        if P2 == "S":
            S1 += 1
        elif P2 == "P":
            S2 += 1
    elif P1 == "S":
        if P2 == "P":
            S1 += 1
        elif P2 == "R":
            S2 += 1
    elif P1 == "P":
        if P2 == "R":
            S1 += 1
        elif P2 == "S":
            S2 += 1
    k += 1
    if S1 == m or S2 == m:
        if S1 == m:
            print(S1,S2,"\nPlayer 1 wins")
        elif S2 == m:
            print(S1,S2,"\nPlayer 2 wins")
        break
    if k == (3*m):
        print(S1,S2,"\nTie")
        break