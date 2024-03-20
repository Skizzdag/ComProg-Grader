#07_Rot13
strlist = []
lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
upper = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".upper()
prepare = ""
result = []
while True:
    inp = input("")
    if inp == "end":
        break
    else:
        strlist.append(inp)
for i in strlist:
    for j in i:
        if j in lower:
            prepare += lower[lower.index(j)+13]
        elif j in upper:
            prepare += upper[upper.index(j)+13]
        else:
            prepare += j
    result.append(prepare)
    prepare = ""
            
print(*result, sep="\n")