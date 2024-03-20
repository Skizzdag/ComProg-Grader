#08_​Nicknames
numkeep = int(input())
name = {}
for i in range(numkeep):
    fristname, nickname = input().split()
    name[fristname] = nickname
    name[nickname] = fristname

numcheck = int(input())
namecheck = []
for j in range(numcheck):
    namecheck.append(input())
    
for k in namecheck:
    if k in name:
        print(name[k])
    else:
        print("Not found")