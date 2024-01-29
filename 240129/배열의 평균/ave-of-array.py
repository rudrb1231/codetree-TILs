arr=[
    list(map(int,input().split()))
    for _ in range(2)
]

for i in range(2):
    v=0
    for j in range(4):
        v+=arr[i][j]
        print(f"{v:.1f}",end=' ')
    print()