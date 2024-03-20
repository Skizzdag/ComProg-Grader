#Part-I-RLE
mode = input()
if mode not in ["str2RLE","RLE2str"]:
    print("Error")
else:
    inp = input()
    prepare_RLE = []
    prepare_str = ""
    count = 0
if mode == "str2RLE":
    for i in range(len(inp)):
        if i+1 != len(inp):
            if inp[i] == inp[i+1]:
                count += 1
            else:
                count += 1
                prepare_RLE.append(inp[i])
                prepare_RLE.append(count)
                count = 0
        else:
            count += 1
            prepare_RLE.append(inp[i])
            prepare_RLE.append(count)
            count = 0
    print(*prepare_RLE)
elif mode == "RLE2str":
    inp = inp.split()
    for i in range(0,len(inp),2):
        if i+1 != len(inp):
            prepare_str += inp[i]*int(inp[i+1])
    print(prepare_str)