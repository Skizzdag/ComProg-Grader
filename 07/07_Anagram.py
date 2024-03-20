#07_Anagram
list_str1 = input().split()
list_str2 = input().split()
str1,str2 = "",""
for s1 in list_str1:
    str1 += s1
for s2 in list_str2:
    str2 += s2
check = "YES"
for i in str1.lower():
    if str1.lower().count(i) != str2.lower().count(i):
        check = "NO"
    if check == "NO":
        break
print(check)