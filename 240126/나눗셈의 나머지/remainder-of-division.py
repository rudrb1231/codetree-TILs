count_arr=[0]*10
a,b=list(map(int,input().split()))
sum_val=0

while a !=0:
    a=a//b
    count_arr[a%b] +=1


for i in range(10):
    sum_val += (count_arr[i]**2)

print(sum_val)