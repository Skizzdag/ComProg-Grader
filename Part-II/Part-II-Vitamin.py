n = int(input()) # อ่ำนจ ำนวนผลไม้
v = [input().split() for i in range(n)]
c = input().split() # อ่ำนค ำสั่งที่ต้องกำรประมวลผล
if c[0] == 'show' :
    for i in v:
        print(*i, sep=" ")
elif c[0] == 'max' :
    vm_list = []
    vm_dict = {}
    for i in v:
        vm_list.append(i[int(c[1])])
        vm_dict[i[0]] = i[int(c[1])]
    result = []
    while len(vm_list) > 0 and len(result) < len(vm_dict):
        prepare = []
        vitamin_max = max(vm_list)
        for i in vm_dict:
            if vm_dict[i] == vitamin_max:
                prepare.append(i)
        prepare.sort()
        for j in prepare:
            result.append(j)
        vm_list.remove(vitamin_max)
    print(result[0],vm_dict[result[0]])
elif c[0] == 'avg' :
    #print(v[int(c[1])-1][1::])
    vitamin_sum = 0.0
    for i in v:
        vitamin_sum += float(i[int(c[1])])
    print( round(vitamin_sum/(len(v)), 4) )
elif c[0] == 'get' :
    vm_dict = {}
    for i in v:
        vm_dict[i[0]] = i[1::]
    if c[1] in vm_dict:
        print(c[1],*vm_dict[c[1]], sep=" ")
    else:
        print(c[1] + " not found")
elif c[0] == 'sort' :
    vm_list = []
    vm_dict = {}
    for i in v:
        if i[int(c[1])] not in vm_list:
            vm_list.append(i[int(c[1])])
        vm_dict[i[0]] = i[int(c[1])]
    result = []
    while len(vm_list) > 0 and len(result) < len(vm_dict):
        prepare  = []
        vitamin_min = min(vm_list)
        for j in vm_dict:
            if vitamin_min == vm_dict[j]:
                prepare.append(j)
            prepare.sort()
        for k in prepare:
            result.append(k)
        vm_list.remove(vitamin_min)
        print(result)
    print(*result, sep=" ")
    