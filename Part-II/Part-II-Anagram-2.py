A = input()
A_lower = A.lower()
B = input()
B_lower = B.lower()
A_edit = {}
B_edit = {}
#เตรียมตัวที่จะแก้
for i in A_lower:
    if "a" <= i <= "z":
        if A_lower.count(i) > B_lower.count(i):
            A_edit[i] = A_lower.count(i) - B_lower.count(i)
for i in B_lower:
    if "a" <= i <= "z":
        if B_lower.count(i) > A_lower.count(i):
            B_edit[i] = B_lower.count(i) - A_lower.count(i)
#เรียงตัวที่แก้ตามพจนานุกรม
A_keys = list(A_edit.keys())
A_keys.sort()
A_dict = {i: A_edit[i] for i in A_keys}
B_keys = list(B_edit.keys())
B_keys.sort()
B_dict = {i: B_edit[i] for i in B_keys}

if len(A_edit) == 0 and len(B_edit) == 0:
    print(A)
    print(" - None")
    print(B)
    print(" - None")
else:
    print(A)
    for i in A_dict:
        if int(A_dict[i]) > 1:
            print(" - remove", A_dict[i], i+"'s")
        else:
            print(" - remove", A_dict[i], i)
    if len(A_dict) == 0:
            print(" - None")
    print(B)
    for i in B_dict:
        if int(B_dict[i]) > 1:
            print(" - remove", B_dict[i], i+"'s")
        else:
            print(" - remove", B_dict[i], i)
    if len(B_dict) == 0:
            print(" - None")