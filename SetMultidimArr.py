liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
m =[]
def ayristir(liste):
    for k in liste:
        if type(k) != list:
            m.append(k)
        else: 
            ayristir(k)
    return m
                

print(ayristir(liste))