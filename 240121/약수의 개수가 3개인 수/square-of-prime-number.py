start, end= tuple(map(int,input().split()))
ans=0


for i in range(start, end+1):
    cont=0
    for j in range(1,i+1):
        if i%j==0:
            cont+=1
    

    if cont==3:
        ans+=1
print(ans)