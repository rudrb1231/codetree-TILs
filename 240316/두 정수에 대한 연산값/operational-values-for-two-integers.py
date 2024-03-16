a,b=list(map(int,input().split()))

def calculate(a,b):
    if a>b:
        a+=25
        b*=2
        print(a,b)
    else:
        b+=25
        a*=2
        print(a,b)


calculate(a,b)