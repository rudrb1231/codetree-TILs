n=int(input())
d=0
cnt=0
arr1= []
for i in range(n):
    arr=input()
    d+=len(arr)
    if arr[0]=='a':
        cnt+=1
print(d,cnt )