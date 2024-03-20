def Digits(number):
    Count = [number.count("0"),number.count("1"),number.count("2"),number.count("3"),number.count("4"),number.count("5"),number.count("6"),number.count("7"),number.count("8"),number.count("9")]
    opt = ""
    n = 0
    for i in Count:
        if i == 0:
            opt += str(n)+','
        n += 1
    opt = opt.strip(",")
    if len(opt) > 0:
        return print(opt)
    else:
        return print("None")
Digits(str(input()))