#06_Binary_Adder
a,b = input().split()
sumab = int(a, 2) + int(b, 2)
print(bin(sumab)[2::])