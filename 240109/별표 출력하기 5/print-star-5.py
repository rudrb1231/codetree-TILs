n=int(input())


for i in range(n):
    for _ in range(n-i,0,-1):
        print('*'*(n-i),end=' ')
    print()