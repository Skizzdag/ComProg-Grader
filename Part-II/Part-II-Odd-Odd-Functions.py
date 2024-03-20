#Part-II-Odd-Odd-Functions
def is_odd(n):
    # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    if n%2 != 0:
        return True
    return False
def has_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่
    for i in x:
        if is_odd(i) == True:
            return True
    return False
def all_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่
    count = 0
    for i in x:
        if is_odd(i) == True:
            count += 1
    if count == len(x):
        return True
    return False
def no_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย
    count = 0
    for i in x:
        if is_odd(i) == False:
            count += 1
    if count == len(x):
        return True
    return False
def get_odds(x):
    # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
    # เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]
    result = []
    for i in x:
        if is_odd(i) == True:
            result.append(i)
    return result
def zip_odds(a, b):
    # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
    # เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
    # [1,19,5,11,7,17,9,3]
    a = get_odds(a)
    b = get_odds(b)
    result = []
    for i in range(len(a)+len(b)):
        if len(a)-i > 0 and len(b)-i > 0:
            result.append(a[i])
            result.append(b[i])
        elif len(a)-i <= 0 and len(b)-i > 0:
            result.append(b[i])
        elif len(a)-i > 0 and len(b)-i <= 0:
            result.append(a[i])
    return result
exec(input().strip())