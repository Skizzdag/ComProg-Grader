def major(stu1,stu2):
    Grade_alphabet = ["A","B","C","D","F"]
    Grade_number = [4,3,2,1,0]
    #Student_Info 1
    GPAX_1 = float(stu1[1])
    com_1 = Grade_number[Grade_alphabet.index(stu1[2])]
    cal1_1 = Grade_number[Grade_alphabet.index(stu1[3])]
    cal2_1 = Grade_number[Grade_alphabet.index(stu1[4])]
    #Student_Info 2
    GPAX_2 = float(stu2[1])
    com_2 = Grade_number[Grade_alphabet.index(stu2[2])]
    cal1_2 = Grade_number[Grade_alphabet.index(stu2[3])]
    cal2_2 = Grade_number[Grade_alphabet.index(stu2[4])]
    #start_check
    varcheck_1 = 0
    varcheck_2 = 0
    #student_1 requ.
    if not com_1 == 4:
        varcheck_1 +=1
    if cal1_1 in [0,1]:
        varcheck_1 +=1
    if cal2_1 in [0,1]:
        varcheck_1 +=1
    #student_2 requ.
    if not com_2 == 4:
        varcheck_2 +=1
    if cal1_2 in [0,1]:
        varcheck_2 +=1
    if cal2_2 in [0,1]:
        varcheck_2 +=1
    #check requ.
    if varcheck_1 > 0 and varcheck_2 > 0:
        return print("None")
    elif varcheck_1 == 0 and varcheck_2 > 0:
        return print(stu1[0])
    elif varcheck_1 > 0 and varcheck_2 == 0:
        return print(stu2[0])
    #compare grade
    elif varcheck_1 == 0 and varcheck_2 == 0:
        #GPAX
        if GPAX_1 == GPAX_2:
            #Cal1
            if cal1_1 == cal1_2:
                #Cal2
                if cal2_1 == cal2_2:
                    return print("Both")
                #cal2
                elif cal2_1 > cal2_2:
                    return print(stu1[0])
                elif cal2_1 < cal2_2:
                    return print(stu2[0])
            #Cal1
            elif cal1_1 > cal1_2:
                return print(stu1[0])
            elif cal1_1 < cal1_2:
                return print(stu2[0])
        #GPAX
        elif GPAX_1 > GPAX_2:
            return print(stu1[0])
        elif GPAX_1 < GPAX_2:
            return print(stu2[0])
major(input().split(),input().split())