inp=input()

arr=inp.split()

a=int(arr[0])
b=int(arr[1])
c=0
for i in range(a,b+1):
    if i%6==0 and i%8 !=0:
        c+=i
print(c)