lower = "abcdefghijklmnopqrstuvwxyz"
upper = "abcdefghijklmnopqrstuvwxyz".upper()
num = "01234567890"
l1 = "!@#$%^&*()_+"
l2 = "qwertyuiop"
l3 = "asdfghjkl"
l4 = "zxcvbnm"
def no_lowercase(t): # return True if no lowercase, otherwise return False
    for i in t:
        if i in lower:
            return True
    return False
def no_uppercase(t):
    for i in t:
        if i in upper:
            return True
    return False
def no_number(t):
    for i in t:
        if i in num:
            return True
    return False
def no_symbol(t):
    for i in t:
        if i in " !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~":
            return True
    return False
def character_repetition(t):
    i = 0
    count = 0
    while i < len(t):
        for j in t[i:i+4].lower():
            if j == t[i].lower():
                count += 1
        if count == 4:
            return False
        else:
            count = 0
        i += 1
    return True
def number_sequence(t):
    i = 0
    while i < len(t)-3:
        if t[i:i+4].lower() in num  or t[i:i+4].lower() in num[::-1]:
            return False
        i += 1
    return True
def letter_sequence(t):
    i = 0
    while i < len(t)-3:
        if t[i:i+4].lower() in  lower or t[i:i+4].lower() in  lower[::-1]:
            return False
        i += 1
    return True

def keyboard_pattern(t):
    i = 0
    while i < len(t)-3:
        if t[i:i+4].lower() in  l1 or t[i:i+4].lower() in  l1[::-1]:
            return False
        elif t[i:i+4].lower() in  l2 or t[i:i+4].lower() in  l2[::-1]:
            return False
        elif t[i:i+4].lower() in  l3 or t[i:i+4].lower() in  l3[::-1]:
            return False
        elif t[i:i+4].lower() in  l4 or t[i:i+4].lower() in  l4[::-1]:
            return False
        i += 1
    return True
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw) == False:
    errors.append("No lowercase letters")
if no_uppercase(passw) == False:
    errors.append("No uppercase letters")
if no_number(passw) == False:
    errors.append("No numbers")
if no_symbol(passw) == False:
    errors.append("No symbols")
if character_repetition(passw) == False:
    errors.append("Character repetition")
if number_sequence(passw) == False:
    errors.append("Number sequence")
if letter_sequence(passw) == False:
    errors.append("Letter sequence")
if  keyboard_pattern(passw) == False:
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    print(*errors, sep="\n")