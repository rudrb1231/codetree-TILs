n=int(input())


for i in range(n):
    for j in range(n):
        if i%2==0:
            print(1+i*n+j,end=' ')
        else:
            print(i*n+n-j,end=' ')
    print()