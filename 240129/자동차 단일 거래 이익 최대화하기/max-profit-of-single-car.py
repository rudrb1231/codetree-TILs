n=int(input())

arr=list(map(int,input().split()))


max_ben=0
min_buy=100
ben=[]
for i in range(n):
    if n==1:
        break

    if arr[i]<min_buy:
        min_buy=arr[i]
    
    if min_buy<arr[i]:
        max_ben=arr[i]-min_buy
        ben.append(max_ben)

for elem in ben:
    if elem>max_ben:
        max_ben=elem

print(max_ben)