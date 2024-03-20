#05_Upgrade
def Upgrade():
    id_s = []
    grade_s = []
    while True:
        inp = input().split()
        if inp == ["q"]:
            break
        id_s.append(inp[0])
        grade_s.append(inp[1])
    uid_s = input().split()
    grade_check = ["F","D","D+","C","C+","B","B+","A"]
    for i in uid_s:
        if grade_s[id_s.index(i)] == "A":
            pass
        else:
            grade_s[id_s.index(i)] = grade_check[grade_check.index(grade_s[id_s.index(i)])+1]
    for j in range(len(id_s)):
        print(id_s[j],grade_s[j])
Upgrade()