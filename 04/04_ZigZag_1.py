def Zig(n):
    number = ""
    for i in range(n):
        value = input()
        number = number+"\n"+value
    number = list(map(int,(number.split())))
    status = input()
    True_line = []
    False_line = []
    order_Even = True
    order_odd = False
    for i in number:
        if number.index(i)%2 == 0 and order_Even == True:
            True_line.append(i)
            order_Even = False
            if number.count(i)>1:
                number[number.index(i)] = "a"
        elif number.index(i)%2 != 0 and order_odd == False:
            False_line.append(i)
            order_odd = True
            if number.count(i)>1:
                number[number.index(i)] = "a"
        elif number.index(i)%2 == 0 and order_Even == False:
            False_line.append(i)
            order_Even = True
            if number.count(i)>1:
                number[number.index(i)] = "a"
        elif number.index(i)%2 != 0 and order_odd == True:
            True_line.append(i)
            order_odd = False
            if number.count(i)>1:
                number[number.index(i)] = "a"
    if status == 'Zig-Zag':
        return print(min(True_line),max(False_line))
    elif status == 'Zag-Zig':
        return print(min(False_line),max(True_line))
Zig(int(input()))