n1,n2= list(map(int,input().split()))

A=list(map(int,input().split()))

B=list(map(int,input().split()))

idx= 0

for i in range(0,n1-n2):
    if A[i:i+n2] == B:
        print('Yes')
        idx+=1
if idx == 0:
    print('No')