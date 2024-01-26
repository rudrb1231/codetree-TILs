n,m=list(map(int,input().split()))

arr=list(map(int,input().split()))
cnt=0
for elem in arr:
    if elem==m:
        cnt+=1

print(cnt)