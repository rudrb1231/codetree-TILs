def is_prime(n):
    if n==1:
        return False


    for i in range(2, n):
        if n%i ==0:
            return False
    return True


def each(n):
    if ((n%10)+(n//10))%2==0:
        return True
    else:
        return False

a,b=tuple(map(int,input().split()))
cnt=0

for i in range(a,b+1):
    if is_prime(i) and each(i):
        cnt+=1

print(cnt)