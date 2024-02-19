A=input().split()
l=A[0]
q=int(A[1])
for i in range(q):
    n=int(input())

    if n==1:
        l=l[1:]+l[0]
        print(l)
    elif n==2:
        l=l[-1]+l[0:-1]
        print(l)
    else:
        l=list(l)
        l.reverse()
        print(''.join(l))