#Part-I-Flowchart-03
import math
a,b,c,d = list(map(int,input().split()))
if a == 1:
    c,d = d,c
    if b == 1:
        c = c+d
    elif b == 2:
        c = c-d
    elif b != 3:
        c = c + c**d
    else:
        c = c/d
    a = (d+(((c/b)**3)+d)**0.5)/(2+b*d)
else:
    if a == 2:
        if b > 1:
            c = c+d
        if b > 2:
            c = c/d
        if b > 3:
            c = c+c**d
        else:
            a = math.log10(c)
    else:
        while a > d:
            a = a -2
            if a < b:
                break
            else:
                c = c+a
print(a,b,c,d)