#07_​DNA
def DNA(strDNA,oper):
    count_check = 0
    operR = ""
    for i in ["A","T","G","C"]:
        count_check += strDNA.count(i)
    if count_check != len(strDNA):
        return print("Invalid DNA")
    elif oper == "R":
        for i in strDNA[::-1]:
            if i == "A":
                operR += "T"
            elif i == "T":
                operR += "A"
            elif i == "G":
                operR += "C"
            elif i == "C":
                operR += "G"
        return 
    elif oper == "F":
        return print("A="+str(strDNA.count("A"))+",","T="+str(strDNA.count("T"))+",","G="+str(strDNA.count("G"))+",","C="+str(strDNA.count("C")))
    elif oper == "D":
        pattern = input()
        prepare = ""
        j = 0
        count = 0
        while j < len(strDNA):
            if strDNA[j:j+2] == pattern:
                count+=1
            j += 1
        return print(count)
DNA(input().strip().upper(),input().strip().upper())