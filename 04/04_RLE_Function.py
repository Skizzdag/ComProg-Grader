def RLE(t):
    prepare = []
    amount = 0
    for i in range(len(t)):
        listin = [] 
        if i+1 < len(t):
            if t[i] != t[i+1]:
                amount +=1
                listin.append(t[i])
                listin.append(amount)
                prepare.append(listin)
                amount = 0
            else:
                amount +=1
        else:
            amount +=1
            listin.append(t[i])
            listin.append(amount)
            prepare.append(listin)
            amount = 0
    return prepare
exec(input())