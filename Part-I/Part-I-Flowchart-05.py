#Part-I-Flowchart-05
c = input().strip()
if c == "S":
    m = int(input())
    q,r,t,k,n,x,i,p = 1,0,1,1,3,3,0,""
    while i < m:
        if 4*q + r - t < n*t:
            p = p + str(n)
            i += 1
            a = 10*(r-n*t)
            n = (10*(3*q+r))//t-10*n
            q = 10*q
            r = a
        else:
            a = (2*q+r)*x
            b = (7*q*k + 2 + x*r)//(x*t)
            q = k*q
            t = x*t
            x += 2
            k += 1
            n = b
            r = a
    p = p[0] + '.' + p[1:]
    print("pi =", p)
else:
    if c == "R":
        n = int(input())
        sigma = 0
        for i in range(0,n+1):
            sigma += ((-3)**(-i))/((2*i)+1)
        p = round(((12)**0.5)*sigma,12)
        print("pi =", p)
    elif c == "P":
        p = round((7+(6+(5)**0.5)**0.5)**0.5,6)
        print("pi =", p)
    else:
        print("Invalid")