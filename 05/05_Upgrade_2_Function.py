#05_​Upgrade_​2 (Function)
def index_of(grades, ID):
    check = []
    for i in range(len(grades)):
        if grades[i][0] == ID:
            check.append(i)
        else:
            check.append(-1)
    for j in check:
        if j != -1:
            return j
    return -1
        

def upgrade(grades, IDs):
    grade_check = ["F","D","D+","C","C+","B","B+","A"]
    IDc = []
    for j in IDs:
        if index_of(grades, j) == -1:
            pass
        else:
            IDc.append(j)
    for i in IDc:
        if grades[index_of(grades, i)][1] == "A":
            pass
        else:
            grades[index_of(grades, i)][1] = grade_check[grade_check.index(grades[index_of(grades, i)][1])+1]
    grades.sort()
exec(input())
exec(input())
exec(input())
