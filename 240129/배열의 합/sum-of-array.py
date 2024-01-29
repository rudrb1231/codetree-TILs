arr_2d=[]

for i in range(4):
    arr_1d=list(map(int,input().split()))
    p=sum(arr_1d)
    arr_2d.append(p)
for i in range(4):
    print(arr_2d[i])