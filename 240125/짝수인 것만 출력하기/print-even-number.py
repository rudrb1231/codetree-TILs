n=int(input())
arr=list(map(int,input().split()))
arr1=[]

for i in range(n):
    if arr[i]%2==0:
        arr1.append(arr[i])
    
for elem in arr1:
    print(elem, end=' ')