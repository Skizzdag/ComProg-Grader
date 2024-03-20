def is_prime(n):
    # ทดสอบว่า n เป็นจำนวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
# คืนจำนวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
    i = 0
    test = False
    while True:
        if  test == False:
            test = is_prime(N+i)
            if N+i == N:
                test = False
            i += 1
        else:
            return N+i-1
            break
    
def next_twin_prime(N):
    # คืนจำนวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
    # twin prime คือจำนวนเฉพาะที่มีค่าต่างกัน 2 เช่น 11 กับ 13 หรือ 41 กับ 43
    Test = [N]
    i = 0
    while True:
        a1 = next_prime(Test[i])
        if a1 not in Test:
            Test.append(a1)
        a2 = next_prime(Test[i+1])
        if a2 not in Test:
            Test.append(a2)
        i+= 1
        if a2-a1 == 2:
            return a1,a2,Test
            break
exec(input().strip())