def Decryption(num):
    Fnum = ""
    Lnum = ""
    str_char = "ABCDEFGHIJ"
    #1
    for i in range(3,32,7):
        Fnum += num[i]
    #2
    for j in range(7,32,5):
        Lnum += num[j]
    #3
    sum_num = int(Fnum) + int(Lnum) + 10000
    #4
    select = str(sum_num)[-4:-1]
    #5
    list_select = sum(list(map(int, select)))
    #6
    char = str(str_char[int(str(list_select)[-1])])
    #7
    return print(select+char)
    
num = str(input())
Decryption(num)