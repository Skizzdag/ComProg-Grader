def grading(s):
    if s>= 80:
        return print("A")
    elif s>= 70:
        return print("B")
    elif s>= 60:
        return print("C")
    elif s>= 50:
        return print("D")
    else:
        return print("F")
grading(float(input()))