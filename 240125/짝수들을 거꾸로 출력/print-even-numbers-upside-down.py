n=int(input())

arr=list(map(int,input().split()))

arr1=[]
for elem in arr:
    if elem%2==0:
        arr1.append(elem)

arr1_reversd=arr1[::-1]
for i in arr1_reversd:
    print(i,end=' ')