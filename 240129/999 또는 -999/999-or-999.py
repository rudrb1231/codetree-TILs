arr=list(map(int,input().split()))

arr1=[]
for elem in arr:
    if elem== 999 or elem==-999:
        break
    arr1.append(elem)    


print(max(arr1),min(arr1))