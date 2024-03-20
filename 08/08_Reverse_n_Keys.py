#08_Reverse_n_Keys
def reverse(d):
    nd = {}
    for i in d:
        nd[d[i]] = i
    return nd
def keys(d,v):
    keylist = []
    for i in d:
        if d[i] == v:
            keylist.append(v)
    return keylist
exec(input().strip())