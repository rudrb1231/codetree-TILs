arr=list(map(int,input().split()))
sum_val=0
cnt=0
for elem in arr:
    if elem==0:
        break    
    sum_val+= elem
    cnt+=1


avg=sum_val/cnt
print(f"{sum_val} {avg:0.1f}")