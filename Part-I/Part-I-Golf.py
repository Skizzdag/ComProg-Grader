#Part-I-Golf
import math
inp_list = []
par_total = 0
stroke_total = 0
stroke_amend = 0
for i in range(9):
    inp_list.append(list(map(int,input().split())))
for p,s,c in inp_list:
    par_total += p
    stroke_total += s
    if c == 1:
        stroke_amend += min(p+2, s)
handicap = math.floor(float(0.8*(1.5*stroke_amend-par_total)))
final_score = stroke_total - handicap
print(stroke_total)
print(handicap)
print(final_score)