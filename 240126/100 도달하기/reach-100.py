n=int(input())


arr=[1,n]


for i in range(1,100):
    arr.append(arr[i]+arr[i-1])
    if arr[i]+arr[i-1]>=100:
        break

for elem in arr:

    print(elem,end=' ')