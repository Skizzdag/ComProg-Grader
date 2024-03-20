def CitizenID(n):
    n_sum = 0
    for i in range(12):
        n_sum += (13-i)*(int(n[i]))
    n12 = (11-(n_sum)%11)%10
    return print(n[0]+" "+n[1:5]+" "+n[5:10]+" "+n[10:12]+" "+str(n12))

CitizenID(str(input("")))