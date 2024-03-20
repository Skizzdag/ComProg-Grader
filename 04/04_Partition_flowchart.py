def Partition(d):
    p = d[-1]
    i = -1
    j = 0
    n = len(d)
    while j < n-1:
        if d[j] <= p :
            i += 1
            numi = d[i]
            numj = d[j]
            d[i] = numj
            d[j] = numi
        j += 1
    num1 = d[i+1]
    num2 = d[-1]
    d[i+1] = num2
    d[-1] = num1
    return print(d)
Partition([int(e) for e in input().split()])