def peaks(x):
    peaks = []
    n = 0
    while True:
        preparelst = x[0+n:3+n]
        if len(preparelst) == 3:
            if preparelst[1] > preparelst[0] and preparelst[1] > preparelst[2]:
                peaks.append(1+n)
        else:
            break
        n += 1
    return peaks
exec(input())

