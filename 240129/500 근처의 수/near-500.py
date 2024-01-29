arr=list(map(int,input().split()))

c=500

max_val=0
p=[]
min_val=0
d=[]

for elem in arr:
    if elem<c:
        p.append(elem)
    else:
        d.append(elem)

print(max(p),min(d))