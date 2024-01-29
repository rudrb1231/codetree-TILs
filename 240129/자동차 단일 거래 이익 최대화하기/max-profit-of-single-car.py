n=int(input())

arr=list(map(int,input().split()))


max_ben=0
min_buy=100
for i in range(n):
    if arr[i]<min_buy:
        min_buy=arr[i]

    if min_buy<arr[i]:
        max_ben=arr[i]-min_buy
print(max_ben)