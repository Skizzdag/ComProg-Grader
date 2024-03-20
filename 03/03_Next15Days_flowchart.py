def Next15Days(d,m,y):
    y -=543
    n = 31
    if m in [4, 6, 9, 11]:
        n = 30
    else:
        if m == 2:
            n = 28
            if y%400 == 0:
                n = 29
            if y%4 == 0 and y%100 ==1:
                n = 29
    d += 15
    if d>n:
        d = d - n
        m = m + 1
    if m>12:
        m = m - 12
        y += 1
    y += 543
    return print(str(d)+"/"+str(m)+"/"+str(y))
Date = [int(e) for e in input().split()]
Next15Days(Date[0],Date[1],Date[2])
    