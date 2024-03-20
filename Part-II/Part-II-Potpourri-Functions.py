def convex_polygon_area(p):
    point = []+p
    point.append(p[0])
    xy = 0
    yx = 0
    for i in range(len(point)-1):
        xy += point[i][0]*point[i+1][1]
        yx += point[i][1]*point[i+1][0]
    Area = 0.5*(xy-yx)
    return abs(Area)
def is_heterogram(s):
    var = s.lower()
    for i in var:
        if var.count(i) > 1 and "a"<=i<="z":
            return False
    return True
def replace_ignorecase(s, a, b):
    i = 0
    check = ""
    result = []
    ans = ""
    while i < len(s):
        check += s[i]
        if len(check) == len(a):
            if check.lower() == a.lower():
                ans += b
                check = ""
            else:
                ans += check[0]
                check = ""+check[1::]
        i += 1
    if len(check) > 0:
        ans += check
    return ans
def top3(votes):
    Vote = []
    for i in votes.values():
        if i not in Vote:
            Vote.append(i)
    Top = []
    while len(Vote) > 0 and len(Top) != 3:
        prepare = []
        Vote_max = max(Vote)
        for j in votes:
            if Vote_max == votes[j]:
                prepare.append(j)
        prepare.sort()
        Vote.remove(Vote_max)
        for k in prepare:
            if len(Top) != 3:
                Top.append(k)
    return Top
for k in range(2):
    exec(input().strip())
