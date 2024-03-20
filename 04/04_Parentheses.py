def Parentheses(inp):
    inp_copy = list(inp)
    for i in range(len(inp)):
        if inp_copy[i] == "(":
            inp_copy[i] = "["
        elif inp_copy[i] == "[":
            inp_copy[i] = "("
        elif inp_copy[i] == ")":
            inp_copy[i] = "]"
        elif inp_copy[i] == "]":
            inp_copy[i] = ")"
    return print(*inp_copy,sep = '')
Parentheses(str(input()))