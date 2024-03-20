#05_UniqueCount
def unique(number):
    number = list(map(int,number.split()))
    number.sort()
    result = [number[0]]
    for i in range(1,len(number)):
        if number[i] != number[i-1]:
            result.append(number[i])
    print(len(result))
    result.sort()
    print(result[0:10])
unique(input())