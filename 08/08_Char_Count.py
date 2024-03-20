#08_Char_Count
char = input().lower()
chardic = {}
for i in char:
    if i not in chardic and "a" <= i <= "z":
        chardic[i] = 1
    elif i in chardic:
        chardic[i] += 1
charlist = []
for j in chardic:
    charlist.append([-chardic[j],j])
charlist.sort()
for v,k in charlist:
    print(k, "->", abs(v))