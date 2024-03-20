def check_number(number):
    if number >= 1 and number%2 == 0:
        print("positive\neven")
    elif number >=1 and number%2 == 1:
        print("positive\nodd")
    elif number <=-1 and number%2 == 0:
        print("negative\neven")
    elif number <=-1 and number%2 == 1:
        print("negative\nodd")
    elif number == 0:
        print("zero\neven")
number = int(input())
check_number(number)