#DICTIONARY listlerden farklı olarak curly parantez kullanır.
#Dictionary key value şeklinde çalışır ve kendi içinde bir dictionary kullanılabilir.
#notlar = {"Ahmet":{"not": 72,"ogrno":13}, "Ece":{"not":65,"ogrno":132}}

#print(notlar["Ahmet"]["not"]) #72

#Eleman eklemek
#notlar["Mert"]={"not":80,"ogrno":125} 

#print(notlar["Mert"]["not"]) #80

#del notlar["Mert"] silme işlemi

#len(notlar) uzunluk


#HACKERRANK

m, n = map(int, input().split())

a = [input() for _ in range(m)]
b = [input() for _ in range(n)]

for i in b:
    if a.count(i)>0:
        for y in range(len(a)):
            if a[y] == i: print(y+1, end=" ")
        print()    
    else:
        print(-1)
"""
n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in b:
    if a.count(i) > 0:
        print(*list(k + 1 for k in range(len(a)) if a[k] == i))
    else:
        print(-1)

"""