def AbbrevNum(num):
    if len(num) <= 3:
        return print(num)
    # 4 - 6 (K)
    elif len(num) > 3 and len(num) <= 6:
        # 4
        if len(num) == 4:
            num_front = num[0]
            num_behide = int(num[1])
            if int(num[2]) >= 5:
                num_behide += 1
            return print(str(num_front)+"."+str(num_behide)+"K")
        # 5
        elif len(num) == 5:
            num_front = num[0]
            num_behide = int(num[1])
            if int(num[2]) >= 5:
                num_behide += 1
            return print(str(num_front)+str(num_behide)+"K")
        # 6
        elif len(num) == 6:
            num_front = num[0:2]
            num_behide = int(num[2])
            if int(num[3]) >= 5:
                num_behide += 1
            return print(str(num_front)+str(num_behide)+"K")
    # 7 - 9 (M)
    elif len(num) > 6 and len(num) <= 9:
        # 7
        if len(num) == 7:
            num_front = num[0]
            num_behide = int(num[1])
            if int(num[2]) >= 5:
                num_behide += 1
            return print(str(num_front)+"."+str(num_behide)+"M")
        # 8
        elif len(num) == 8:
            num_front = num[0]
            num_behide = int(num[1])
            if int(num[2]) >= 5:
                num_behide += 1
            return print(str(num_front)+str(num_behide)+"M")
        # 9
        elif len(num) == 9:
            num_front = num[0:2]
            num_behide = int(num[2])
            if int(num[3]) >= 5:
                num_behide += 1
            return print(str(num_front)+str(num_behide)+"M")
    #10 - 12 (B)
    elif len(num) > 9:
        # 10
        if len(num) == 10:
            num_front = num[0]
            num_behide = int(num[1])
            if int(num[2]) >= 5:
                num_behide += 1
            return print(str(num_front)+"."+str(num_behide)+"B")
        # >10
        elif len(num) > 10:
            num_front = int(num[0:-9])
            if int(num[-10]) >= 5:
                num_front += 1
            return print(str(num_front)+"B")
AbbrevNum(str(input()))