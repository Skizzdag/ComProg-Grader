#06_FourFunctions
def make_int_list(x):
    return list(map(int,x.split()))

def is_odd(e):
    if e%2 == 0:
        return False
    else:
        return True
    
def odd_list(alist):
    blist = []
    for i in alist:
        if is_odd(i) == True:
            blist.append(i)
    return blist

def sum_square(alist):
    suma = 0
    for i in alist:
        suma += i**2
    return suma

exec(input().strip())