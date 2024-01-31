n,m=list(map(int,input().split()))

# 2차원 배열을 구현합니다.
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num=0
# 배열의 숫자를 채웁니다.
for col in range(m):
    if col% 2==0:
        for row in range(n):
            arr[row][col] = num
            num+=1
    else:
        for row in range(n-1,-1,-1):
            arr[row][col] = num
            num+=1

for row in range(n):
    for col in range(m):
        print(arr[row][col],end=' ')
    print()