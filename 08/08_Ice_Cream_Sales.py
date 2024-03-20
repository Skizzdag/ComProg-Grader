#08_Ice_Cream_Sales
goods = {}
for i in range(int(input())):
    icecream,price = input().split()
    goods[icecream] = float(price)

Total_sales = 0
sales = {}
for j in range(int(input())):
    order,amout = input().split()
    if order in goods:
        if order not in sales:
            sales[order] = goods[order]*float(amout) 
        else:
            sales[order] += goods[order]*float(amout) 
        Total_sales += goods[order]*float(amout)

if Total_sales == 0:
    print("No ice cream sales")
else:
    Top_sales_list = []
    for key in sales:
        Top_sales_list.append([sales[key],key])
    print("Total ice cream sales:",float(Total_sales))

    maxsale = []
    for sale,name in Top_sales_list:
        m = max(Top_sales_list)
        if sale == m[0]:
            maxsale.append(name)
    maxsale.sort()
    print("Top sales:",", ".join(maxsale))