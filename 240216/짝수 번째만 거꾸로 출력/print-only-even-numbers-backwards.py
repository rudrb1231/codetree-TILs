A=input()


n=[]

for i in range(len(A)):
    if i%2==1:
        n.append(A[i])
    else:
        continue


for i in range(len(n)-1,-1,-1):
    print(n[i],end='')