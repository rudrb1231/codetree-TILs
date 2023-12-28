n=int(input())
c=0
t=0

for i in range(1,n+1):
    p=int(input())
    c+=p
    t+=1

print(c, f'{c/t:0.1f}')