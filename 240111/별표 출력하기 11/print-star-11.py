n=int(input())

for i in range(2*n+1):
    for j in range(2*n+1):
        if j%2==1 and i%2==1:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()