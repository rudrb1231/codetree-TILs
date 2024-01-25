n=int(input())
arr=[]
cnt=0

for i in range(1,101):
    arr[i]=n*i
    arr.append(arr[i])
    print(arr[i],end=' ')
    if j %5==0:
        cnt+=1
    
    if cnt==2:
        break