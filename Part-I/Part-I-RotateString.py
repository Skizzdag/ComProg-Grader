#RotateString
def RotateStr():
    oper = str(input())
    num = int(input())
    inp = [input().strip() for i in range(num)]
    inp_str = ""
    layer = ""
    for i in inp:
        if len(i) != len(inp[0]):
            return print("Invalid size")
        else:
            inp_str += i
    if oper == "90":
        for i in range(0,len(inp_str)-((num-1)*len(inp[0]))):
            layer += inp_str[i:i+len(inp[0])*len(inp):len(inp[0])]
            print(layer[::-1])
            layer = ""
    elif oper == "180":
        inp_str = inp_str[::-1]
        for i in range(0,len(inp_str),len(inp[0])):
            layer += inp_str[i:i+len(inp[0])]
            print(layer)
            layer = ""
    elif oper == "flip":
        for i in inp:
            print(i[::-1])
RotateStr()