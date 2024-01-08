n=input()
arr=n.split()
a,b,c=int(arr[0]),int(arr[1]),int(arr[2])
sat=True

for i in range (a,b+1):
    if i%c==0:
        sat=False

if sat==True:
    print('YES')
else:
    print('NO')