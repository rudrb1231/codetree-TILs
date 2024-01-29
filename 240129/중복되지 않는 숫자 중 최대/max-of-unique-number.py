import sys
n=int(input())

arr=list(map(int,input().split()))

cnt=0

max_val=max(arr)

for i in range(n):
    if arr[i] == max_val:
        cnt+=1
if cnt>=2:
    print('-1')
else:
    print(max_val)