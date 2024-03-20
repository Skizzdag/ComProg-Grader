#07_Plural
inp = input()
if inp[-1] in ["s","x"] or inp[-2:] == "ch":
    inp += "es"
elif inp[-1] == "y":
    if inp[-2] in ["a","e","i","o","u"]:
        inp += "s"
    else:
        inp = inp[0:-1]+"ies"
else:
    inp += "s"
print(inp)