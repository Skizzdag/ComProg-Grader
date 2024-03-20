def name(number):
    Surename = ["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
    Nickname = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
    Name = [input() for i in range(number)]
    for j in Name:
        if j in Surename:
            print(Nickname[Surename.index(j)])
        elif j in Nickname:
            print(Surename[Nickname.index(j)])
        else:
            print("Not found")
name(int(input()))