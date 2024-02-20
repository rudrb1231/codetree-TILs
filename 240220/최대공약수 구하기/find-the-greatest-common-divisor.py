a,b=map(int,input().split())
def choi(n,m):
    for i in range(min(n,m),2,-1):
        if n%i==0 and m%i==0:
            break
    print(i)
choi(a,b)