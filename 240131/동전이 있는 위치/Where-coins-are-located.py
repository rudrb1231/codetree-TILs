n,m=list(map(int,input().split()))

placed=[[0 for _ in range(n)]for _ in range(n)]

for _ in range(m):
    r,c=tuple(map(int,input().split()))
    placed[r-1][c-1]=1

exists= int(True) if placed[r-1][c-1] ==1 else False

for row in placed:
    for elem in row:
        print(elem,end=' ')
    print()