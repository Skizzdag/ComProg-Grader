def Peaks():
    num = list(map(int, input().split()))
    peaks = 0
    n = 0
    while True:
        preparelst = num[0+n:3+n]
        if len(preparelst) == 3:
            if preparelst[1] > preparelst[0] and preparelst[1] > preparelst[2]:
                peaks += 1
        else:
            break
        n += 1
    return print(peaks)
Peaks()