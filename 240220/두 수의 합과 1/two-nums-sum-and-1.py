a=input().split()
b,c=int(a[0]),int(a[1])

d=str(b+c)
cnt=0


for elem in d:
    if elem=='1':
        cnt+=1

print(cnt)