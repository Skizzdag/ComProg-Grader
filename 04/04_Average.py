def Average():
    sum_number = 0
    k = 0
    while True:
        number = str(input())
        if number == "q":
            if k == 0:
                return print("No Data")
                break
            else:
                return print(round(sum_number/k, 2))
                break
        else:
            sum_number += float(number)
            k += 1
Average()