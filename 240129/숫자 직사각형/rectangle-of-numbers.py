n,m=list(map(int,input().split()))

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

num=0

for i in range(n):
    for j in range(m):
        arr[i][j]=num
        num+=1
        print(num,end=' ')
    print()