n=int(input())
cnt=0

for i in range(n):
    arr=list(map(int,input().split()))
    sum_val=0
    for elem in arr:
        sum_val+=elem
        avg=sum_val/4
    if avg>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)