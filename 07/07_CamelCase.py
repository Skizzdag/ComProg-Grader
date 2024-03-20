#07_CamelCase
inp = input("")+" "
result = ""
prepare = ""
for i in inp:
    if i not in "\"\'/\\().,;:-<> ":
        prepare += i
    else:
        result += " " + prepare
        prepare = ""
result = result.strip().split()
for i in range(len(result)):
    if i == 0:
        result[i] = result[i].lower()
    else:
        result[i] = result[i].capitalize()
print(*result, sep="")