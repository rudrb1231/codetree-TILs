count_arr=[0]*11

arr=list(map(int,input().split()))

for elem in arr:
    if elem==0:
        break
    count_arr[elem//10]+=1
for i in range(10,0,-1):
    print(f"{i*10} - {count_arr[i]}")