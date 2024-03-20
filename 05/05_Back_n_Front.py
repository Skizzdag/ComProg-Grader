def BacknFront():
    #prepare_data
    data1 = [int(input()) for i in range(int(input()))]
    data2 = list(map(int,input().split()))
    data3 = []
    while True:
        inp = int(input())
        if inp != -1:
            data3.append(inp)
        else:
            break
    data = data1+data2+data3
    #prepare_result
    result = []
    n = 0
    for i in data:
        preparelst = [i]
        if n%2 == 0:
            result = result + preparelst
        else:
            result = preparelst + result
        n += 1
    return print(result)
BacknFront()