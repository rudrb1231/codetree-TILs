n,m=list(map(int,input().split()))

placed=[[0for _ in range(n)]for _ in range(n)]
cnt=1
for i in range(m):
    r,c=tuple(map(int,input().split()))
    placed[r-1][c-1]=True

for i in range(n):
    for j in range(n):
        if placed[i][j]==int(True):
            placed[i][j]=cnt
            cnt+=1
        


for row in placed:
    for elem in row:
        print(elem,end=' ')
    print()