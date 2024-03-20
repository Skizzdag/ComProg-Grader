#05_Third_Closest
def Third_Closest():
    point = []
    for i in range(int(input())):
        result = []
        x,y = input().split()
        D = ((float(x)-0)**2+(float(y)-0)**2)**0.5
        result = [D,i+1,float(x),float(y)]
        point.append(result)
    point.sort()
    return print("#"+str(point[2][1])+":","("+str(point[2][2])+","+" "+str(point[2][3])+")")
Third_Closest()