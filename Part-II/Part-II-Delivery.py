order = []
while True:
    inp = input().split()
    if inp[0] == "END":
        break
    inp[2] = int(inp[2])
    inp[3] = int(inp[3])
    inp[4] = int(inp[4])
    order.append(inp)
no_error = []    
for i in order:
    Date = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (int(i[4])-543)%400 == 0:
        Date = [31,29,31,30,31,30,31,31,30,31,30,31]
    elif (int(i[4])-543)%4 == 0 and (int(i[4])-543)%100 != 0:
        Date = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    if int(i[4]) < 2558:
        print("Error:",*i,sep=" ",end=" ")
        print("--> Invalid year")
    elif not(1 <= int(i[3]) <= 12):
        print("Error:",*i,sep=" ",end=" ")
        print("--> Invalid month")
    elif int(i[2]) > Date[int(i[3])-1] or int(i[2]) < 1:
        print("Error:",*i,sep=" ",end=" ")
        print("--> Invalid date")
    elif i[1] not in ["E","Q","N","F"]:
        print("Error:",*i,sep=" ",end=" ")
        print("--> Invalid delivery type")
    else:
        no_error.append(i[::-1])

for i in no_error:
    Date = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (int(i[0])-543)%400 == 0:
        Date = [31,29,31,30,31,30,31,31,30,31,30,31]
    elif (int(i[0])-543)%4 == 0 and (int(i[0])-543)%100 != 0:
        Date = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    if i[3] == "E":
        i[2] = int(i[2]) + 1
        if int(i[2]) > Date[int(i[1])-1]:
            i[2] = 1
            i[1] = int(i[1]) + 1
        if int(i[1]) > 12:
            i[1] = 1
            i[0] = int(i[0]) + 1
    elif i[3] == "Q":
        i[2] = int(i[2]) + 3
        if int(i[2]) > Date[int(i[1])-1]:
            i[2] = i[2] - Date[int(i[1])-1]
            i[1] = int(i[1]) + 1
        if int(i[1]) > 12:
            i[1] = 1
            i[0] = int(i[0]) + 1
    elif i[3] == "N":
        i[2] = int(i[2]) + 7
        if int(i[2]) > Date[int(i[1])-1]:
            i[2] = i[2] - Date[int(i[1])-1]
            i[1] = int(i[1]) + 1
        if int(i[1]) > 12:
            i[1] = 1
            i[0] = int(i[0]) + 1
    elif i[3] == "F":
        i[2] = int(i[2]) + 14
        if int(i[2]) > Date[int(i[1])-1]:
            i[2] = i[2] - Date[int(i[1])-1]
            i[1] = int(i[1]) + 1
        if int(i[1]) > 12:
            i[1] = 1
            i[0] = int(i[0]) + 1

for i in no_error:
    i.pop(3)
no_error.sort()
for i in no_error:
    print(str(i[-1])+":","delivered on",str(i[2])+"/"+str(i[1])+"/"+str(i[0]))