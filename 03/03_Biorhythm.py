import math
def Biorhythm(bd,bm,by,d,m,y):
    #prepare_by
    by -= 543
    n_by = [31,28,31,30,31,30,31,31,30,31,30,31]
    if by%400 == 0:
        n_by = [31,29,31,30,31,30,31,31,30,31,30,31]
    if by%4 == 0 and by%100 > 0:
        n_by = [31,29,31,30,31,30,31,31,30,31,30,31]
    #prepare_y
    y -= 543
    n = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400 == 0:
        n = [31,29,31,30,31,30,31,31,30,31,30,31]
    if y%4 == 0 and y%100 > 0:
        n = [31,29,31,30,31,30,31,31,30,31,30,31]
    #prepare_red_zone
    red_zone = n_by[bm-1]-bd+1+sum(n_by[bm:])
    #prepare_black_zone
    black_zone = (y-by-1)*365
    #prepare_blue_zone
    blue_zone = sum(n[:m-1])+d-1
    #sum_date
    sum_date = red_zone + black_zone + blue_zone
    return print(sum_date, "{:.2f}".format(math.sin((2*math.pi*sum_date)/23)), "{:.2f}".format(math.sin((2*math.pi*sum_date)/28)), "{:.2f}".format(math.sin((2*math.pi*sum_date)/33)))

date = [int(e) for e in input().split()]
Biorhythm(date[0],date[1],date[2],date[3],date[4],date[5])