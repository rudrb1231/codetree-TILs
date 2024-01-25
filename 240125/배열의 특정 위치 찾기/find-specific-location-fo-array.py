arr=list(map(int,input().split()))

sum_val=0
sum_3=0
n=len(arr)

cnt=0
for i in range (1,n+1,2):
    sum_val+=arr[i]

avg=(arr[2]+arr[5]+arr[8])/3

print(f"{sum_val} {avg:0.1f}")