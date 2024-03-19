n,m=list(map(int,input().split()))
arr=[0]+ list(map(int,input().split()))
a=m


def calcul ():
    global a
    ans=0

    while a:
        ans+=arr[a]
        if a%2==0:
            a=a//2
        else:
            a=a-1
    return ans

        
print(calcul())