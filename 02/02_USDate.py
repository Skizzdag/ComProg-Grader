def US_date(a):
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return print(month[int(a[1])-1] +" ", a[0] + ", " + a[2])
inp = input("").split("/")
US_date(inp)