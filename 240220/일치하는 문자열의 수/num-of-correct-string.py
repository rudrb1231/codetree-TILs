k=input().split()

n,A=int(k[0]),k[1]
cnt=0

for i in range(n):
    m=input()
    if A==m:
        cnt+=1
print(cnt)