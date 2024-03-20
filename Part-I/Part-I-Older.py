#Part-I-Older
person_1 = input().split()
person_2 = input().split()
person_1[2] = person_1[2].strip(",")
person_2[2] = person_2[2].strip(",")
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month.reverse()
#year_check
if int(person_1[3])-int(person_2[3]) < 0:
    print(person_1[0])
elif int(person_1[3])-int(person_2[3]) > 0:
    print(person_2[0])
elif int(person_1[3])-int(person_2[3]) == 0:
    #month_check
    if month.index(person_1[1])-month.index(person_2[1]) > 0:
        print(person_1[0])
    elif month.index(person_1[1])-month.index(person_2[1]) < 0:
        print(person_2[0])
    elif month.index(person_1[1])-month.index(person_2[1]) == 0:
        #day_check
        if int(person_1[2])-int(person_2[2]) < 0:
            print(person_1[0])
        elif int(person_1[2])-int(person_2[2]) > 0:
            print(person_2[0])
        elif int(person_1[2])-int(person_2[2]) == 0:
            print(person_1[0],person_2[0])