a,b=list(map(int,input().split()))

def judge(a,b):

    if a>b:
        a=a*2
        b=b+10
    else:
        b=b*2
        a=a+10

    return a,b

x,y= judge(a,b)

print(x,y)