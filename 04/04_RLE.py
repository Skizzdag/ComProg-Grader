def RLE(inp):
    prepare = []
    amount = 0
    for i in range(len(inp)):
        if i+1 < len(inp):
            if inp[i] != inp[i+1]:
                amount +=1
                prepare.append(inp[i])
                prepare.append(amount)
                amount = 0
            else:
                amount +=1
        else:
            amount +=1
            prepare.append(inp[i])
            prepare.append(amount)
            amount = 0
    return print(*prepare,sep = ' ')
RLE(input())