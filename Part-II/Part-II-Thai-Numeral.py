def to_Thai( N ):
    th_num = {0:"",1:" neung",2:" song",3:" sam",4:" si",5:" ha",6:" hok",7:" chet",
              8:" paet",9:" kao",10:" sip",100:" roi",1000:" pun"}
    out = ""
    et_check = 0
    if N >= 1000:
        out += th_num[N//1000]
        out += " pun"
        N%=1000
        et_check += 1
    if N >= 100:
        out += th_num[N//100]
        out += " roi"
        N%=100
        et_check += 1
    if N>10:
        if N//10 == 2:
            out += " yi sip"
        elif N//10 != 1:
            out += th_num[N//10]+" sip"
        else:
            out += " sip"
        N %= 10
        if N == 1:
            out += " et"
        else:
            out += th_num[N]
        et_check += 1
    elif N<=10:
        if et_check > 0 and N == 1:
            out += " et"
        elif et_check == 0 and N==0:
            out += " soon"
        else:
            out+= th_num[N]
    return out.strip()
exec(input().strip())