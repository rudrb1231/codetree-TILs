inp=input()
m=inp.split()
a,b=int(m[0]),int(m[1])
arr=[a,b]


for i in range(2,10):
    
    arr.append((arr[i-1]+arr[i-2])%10)

for j in range(10):
    print(arr[j],end=' ')