n=int(input())

cnt=0
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j>i:
            print('  ',end='')
        else:
            cnt+=1
            if cnt==10:
                cnt=1
            print(cnt,end=' ')
    print()