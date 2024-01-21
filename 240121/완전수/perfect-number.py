start, end= tuple(map(int, input().split()))
ans=0


for i in range(start, end+1):
    divisor_sum=0
    for divisor in range(1, i):
        if i%divisor==0:
            divisor_sum+=divisor


    if divisor_sum== i :
        ans+=1

print(ans)