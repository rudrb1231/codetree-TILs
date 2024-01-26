count_arr=[0]*10
a,b=list(map(int,input().split()))
sum_val=0
while a>1:
    if a<=1:
        break
    count_arr[a%b] +=1
    a=a//b

for i in range(10):
    sum_val += (count_arr[i]**2)

print(sum_val)