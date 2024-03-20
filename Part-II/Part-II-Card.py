#Part-II-Card
def Card_Sequence(Card):
    Card_list = []
    prepare = ""
    for i in Card:
        prepare += i
        if len(prepare) == 2:
            Card_list.append(prepare)
            prepare = ""
    return Card_list
    
def Card_Value(Card):
    Card_list = Card_Sequence(Card)
    front = {"A":1,"T":10,"J":11,"Q":12,"K":13}
    back = {"C":1,"D":2,"H":3,"S":4}
    card1 = 0
    card2 = 0
    for j in range(len(Card_list)-1):
        if Card_list[j][0] in front:
            card1 = front[Card_list[j][0]]
        else:
            card1 = int(Card_list[j][0])
        if Card_list[j+1][0] in front:
            card2 = front[Card_list[j+1][0]]
        else:
            card2 = int(Card_list[j+1][0])
        if card1 - card2 == 0:
            card1 = back[Card_list[j][1]]
            card2 = back[Card_list[j+1][1]]
            if card1 - card2 < 0:
                print(str(card1-card2), end="")
            elif card1 - card2 > 0:
                print("+"+str(card1-card2), end="")
            elif card1 - card2 == 0:
                print("0",end="")
        elif card1 - card2 < 0:
            print(str(card1-card2), end="")
        elif card1 - card2 > 0:
            print("+"+str(card1-card2), end="")
        else:
            card1 += int(Card_list[j][0])
        card1 = 0
        card2 = 0

Card = Card_Value(input())