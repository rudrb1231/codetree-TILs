n,m=map(int,input().split())


def gong(a,b):
    gdc=1
    for i in range(1,max(m,n)):
        if a%i==0 and b%i==0:
            gdc*=i
    print(gdc)

gong(n,m)