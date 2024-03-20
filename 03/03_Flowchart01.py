def flowchart(a,b,c,d):
    if a>b:
        a,b = b,a
        if d>=a:
            if c>d:
                c = c-a
        else:
            c += a
        b = a+c+d
    else:
        if c>a>=b:
            d += a
        if d>c:
            b += 2
        else:
            b *= 2
    return print(a,b,c,d)
inp = list(map(int, input().split()))
flowchart(inp[0],inp[1],inp[2],inp[3])