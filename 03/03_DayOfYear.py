def DayOfYear(d,m,y):
    #prepare_y
    y -= 543
    #prepare_m
    n = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400 == 0:
        n = [31,29,31,30,31,30,31,31,30,31,30,31]
    if y%4 == 0 and y%100 > 0:
        n = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_m = sum(n[0:m-1])
    #preapre_sum_day
    sum_day = day_m + d
    return print(sum_day)
DayOfYear(int(input()),int(input()),int(input()))