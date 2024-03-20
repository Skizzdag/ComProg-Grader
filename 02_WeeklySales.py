def WeeklySales(a):
    sale_list = list(map(int, a))
    return print(sum(sale_list))
sale = input("").split()
WeeklySales(sale)