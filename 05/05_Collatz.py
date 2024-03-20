def Collatz(n):
    n_lst = []
    while n != 1:
        n_lst.append(n)
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
    n_lst.append(n)
    n_lst = n_lst[-1:-16:-1]
    return print(*n_lst[::-1],sep="->")
Collatz(int(input()))