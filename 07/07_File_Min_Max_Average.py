inp = input().split()
score = []
fn = open(inp[0], "r")
for i in fn:
    sid,point = i.strip().split()
    if sid[:2] == inp[1][2::]:
        score.append(float(point))
fn.close()
if len(score) != 0:
    print(min(score),max(score),sum(score)/len(score))
else:
    print("No data")