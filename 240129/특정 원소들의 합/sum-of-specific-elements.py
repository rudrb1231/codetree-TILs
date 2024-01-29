arr=[list(map(int,input().split())) for _ in range(4)]

v=0
for i in range(4):
    for j in range(i+1):
        v+=arr[i][j]

print(v)