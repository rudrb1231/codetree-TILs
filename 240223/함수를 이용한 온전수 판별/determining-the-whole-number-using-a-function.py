def on(n):
    if n%2==0:
        return False
    elif n%10==5:
        return False
    elif n%3==0 and n%9 !=0:
        return False
    else:
        return True



a,b=tuple(map(int,input().split()))

cnt=0
for i in range(a,b+1):
    if on(i):
        cnt+=1
print(cnt)