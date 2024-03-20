#02_Decimal2Fraction
import math
def Fraction(a):
    #เตรียมตัวเศษ
    all_decimal = a[1]+a[2]
    norepeat_decimal = "0"+a[1]
    numerator = int(all_decimal)-int(norepeat_decimal)
    #เตรียมตัวส่วน
    amout_repeat_decimal = len(a[2])
    amout_norepeat_decimal = len(a[1])
    denominator = ("9"*amout_repeat_decimal)+("0"*amout_norepeat_decimal)
    #เตรียมเศษส่วน
    gcd = math.gcd(int(numerator), int(denominator))
    pre_numerator = int(numerator)//gcd
    fin_denominator = int(denominator)//gcd
    fin_numerator = (int(a[0])*fin_denominator)+pre_numerator
    #พร้อม!!!
    return print(int(fin_numerator),"/",int(fin_denominator))

Decimal = input().split(",") # จำนวนเต็ม, ทศนิยม, ทศนิยมซ้ำ
Fraction(Decimal)