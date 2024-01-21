m=int(input())

for _ in range(m):
    n=int(input())
    cnt=0
    while n!=1:
        if n%2==1:
            n=3*n+1
        else:
            n=n//2
        cnt+=1
    print(cnt)