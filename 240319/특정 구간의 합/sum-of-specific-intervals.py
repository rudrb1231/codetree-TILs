n,m=list(map(int,input().split()))
A=[0]+list(map(int,input().split()))

def calculate():
    global A
    ans=0
    for i in range(a1,a2+1,1):
        ans+=A[i]
    return ans

for i in range(m):
    a1,a2=list(map(int,input().split()))

    print(calculate())