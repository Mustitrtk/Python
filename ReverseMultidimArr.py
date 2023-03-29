def rev(l):
    res=[]
    for i in range(len(l)-1,-1,-1):
        res.append(l[i])

    return res

liste =  [[1, 2], [3, 4], [5, 6, 7]]
m=[]       

for k in liste:
    if type(k)==list:
        m.append(rev(k))
    else:
        m.append(k)

m.reverse()

for i in m:
    print(i, end=" ")