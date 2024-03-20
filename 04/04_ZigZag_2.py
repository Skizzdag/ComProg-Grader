def Zig():
    Redmax = 0
    Bluemax = 0
    Redmin = 0
    Bluemin = 0
    i = 0
    status = ''
    while True:
        inp = input().split()
        if inp[0] == 'Zig-Zag' or inp[0] == 'Zag-Zig':
            status = inp[0]
            break
        x = int(inp[0])
        y = int(inp[1])
        if i%2 == 1:
            x, y = y, x
        if x > Redmax:
            Redmax = x
        elif x < Redmin:
            Redmin = x
        if y > Bluemax:
            Bluemax = y
        elif y < Bluemin:
            Bluemin = y
        i += 1
    if status == 'Zig-Zag':
        return print(Redmin,Bluemax)
    else:
        return print(Bluemin,Redmax)
Zig()