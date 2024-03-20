def missing_digits(t):
    Count = [t.count("0"),t.count("1"),t.count("2"),t.count("3"),t.count("4"),t.count("5"),t.count("6"),t.count("7"),t.count("8"),t.count("9")]
    opt = []
    n = 0
    for i in Count:
        if i == 0:
            opt.append(n)
        n += 1
    return opt
exec(input())