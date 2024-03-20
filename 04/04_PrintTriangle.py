def Triangle(h):
    for i in range(h):
        if i == 0:
            print("."*(h-i-1)+"*")
        elif i+1 == h:
            print("*"*(2*h-1))
        else:
            print("."*(h-i-1)+"*"+"."*(2*(i+1)-3)+"*")
Triangle(int(input()))