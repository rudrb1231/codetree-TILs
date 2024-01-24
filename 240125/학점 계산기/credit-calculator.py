n=int(input())
grad=list(map(float,input().split()))

sum_val=sum(grad)

avg=sum_val/n

print(f"{avg:0.1f}")

if avg>=4.0:
    print('Perfect')
elif avg>=3.0:
    print('Good')
else:
    print('Poor')