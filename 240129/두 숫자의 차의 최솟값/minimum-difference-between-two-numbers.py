n=int(input())

arr=list(map(int,input().split()))

min_sub=100

for i in range(1,n):
    sub=arr[i] - arr[i-1]
    if sub<min_sub:
        min_sub=sub

print(min_sub)