n=int(input())

arr=list(map(int,input().split()))

cnt=0

for i in range(n):
    if cnt==3:
        break
    if arr[i] == 2:
        cnt+=1
    
print(i)