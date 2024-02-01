n=int(input())
d=0
cnt=0
arr1= []
for i in range(n):
    arr=input()
    d+=len(arr)
    for j in range(len(arr)):
        if arr[j]=='a':
            cnt+=1
print(d,cnt )