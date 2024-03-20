data = input()
fn = open(data, "r")

order = fn.readline()
pattern = fn.readline()
apha = {}
for i in pattern.strip("[]").split("["):
    if order == "T2M\n":
        apha[i[0]] = i[2::]
    elif order == "M2T\n":
        apha[i[2::]] = i[0]

if order == "T2M\n":
    apha.pop("\n")
    while True:
        text = list(fn.readline().strip())
        check = 0
        if len(text) == 0:
            break
        for i in text:
            if i not in apha:
                print("Invalid : ",*text, sep = "")
                check += 1
                break
        if check == 0:
            morse = ''
            for e in text:
                morse += " "+apha[e]
            print(morse.strip())
elif order == "M2T\n":
    apha.pop("")
    while True:
        text = fn.readline().strip().split()
        check = 0
        if len(text) == 0:
            break
        for i in text:
            if i not in apha:
                print("Invalid : ",*text, sep=" ")
                check += 1
        if check == 0:
            morse = ""
            for e in text:
                morse += apha[e]
            print(morse.strip())
else:
    print("Invalid code")

fn.close()