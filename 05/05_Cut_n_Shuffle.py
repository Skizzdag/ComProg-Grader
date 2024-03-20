#05_Cut_n_Shuffle
def Cut_Shuffle(card,order):
    for i in order:
        if i == "C":
            front = card[0:len(card)//2]
            back = card[len(card)//2:]
            card = back+front
        elif i =="S":
            front = card[0:len(card)//2]
            back = card[len(card)//2:]
            shuffle = []
            f = 0
            b = 0
            for j in range(len(card)):
                if j%2 == 0:
                    shuffle.append(front[f])
                    f+=1
                elif j%2 != 0:
                    shuffle.append(back[b])
                    b+=1
            card = shuffle
    return print(*card, sep=" ")

Cut_Shuffle(input().split(),list(input()))   