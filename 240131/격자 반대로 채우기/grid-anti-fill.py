n=int(input())


arr=[[0 for _ in range(n)] for _ in range(n)]

cnt=0
if n%2==0:
    for col in range(n-1,-1,-1):
        if col%2==1:
            for row in range(n-1,-1,-1):
                cnt+=1
                arr[row][col]=cnt

        else:
            for row in range(0,n):
                cnt+=1
                arr[row][col]=cnt
if n%2==1:
    for col in range(n-1,-1,-1):
        if col%2==0:
            for row in range(n-1,-1,-1):
                cnt+=1
                arr[row][col]=cnt
        else:
            for row in range(0,n):
                cnt+=1
                arr[row][col]=cnt

                
for a in arr:
    for b in a:
        print(b, end=' ')
    print()