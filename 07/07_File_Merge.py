def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", "" # แฟ้มหมดแล้ว คืนสตริงว่าง
da,db = input().split()
fa = open(da, "r")
fb = open(db, "r")
idsa, gradea = read_next(fa)
idsb, gradeb = read_next(fb)
while True:
    if len(idsa) == 0 and len(idsb) == 0:
        break
    elif len(idsa) == 0:
        print(idsb,gradeb)
        idsb, gradeb = read_next(fb)
    elif len(idsb) == 0:
        print(idsa,gradea)
        idsa, gradea = read_next(fa)
    elif idsa[8:10] == idsb[8:10]:
        if idsa[0:2] < idsb[0:2]:
            print(idsa,gradea)
            idsa, gradea = read_next(fa)
        elif idsa[0:2] > idsb[0:2]:
            print(idsb,gradeb)
            idsb, gradeb = read_next(fb)
        elif idsa[0:2] == idsb[0:2]:
            if gradea > gradeb:
                print(idsb,gradeb)
                idsb, gradeb = read_next(fb)
            elif gradea < gradeb:
                print(idsa,gradea)
                idsa, gradea = read_next(fa)
    elif idsa[8:10] < idsb[8:10]:
        print(idsa,gradea)
        idsa, gradea = read_next(fa)
    elif idsa[8:10] > idsb[8:10]:
        print(idsb,gradeb)
        idsb, gradeb = read_next(fb)
fa.close()
fb.close()