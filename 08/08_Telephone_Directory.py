#08_​Telephone_​Directory
Yellowbook = {}
for i in range(int(input())):
    fristname,lastname,tel = input().split()
    name = fristname+" "+lastname
    Yellowbook[name] = tel
    Yellowbook[tel] = name
for j in range(int(input())):
    inp = input()
    if inp in Yellowbook:
        print(inp,"-->",Yellowbook[inp])
    else:
        print(inp,"-->","Not found")