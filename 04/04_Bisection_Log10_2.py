def log(a):
    L = 0
    U = 0
    b = a
    while b > 0:
        b = b//10
        U += 1
    x = (U+L)/2
    while abs(a-10**x)>=(10**(-10))*max(a,10**x):
        if 10**x > a:
            U = x
        elif 10**x < a:
            L = x
        x = (U+L)/2
    return print(round(x,6))
log(float(input()))