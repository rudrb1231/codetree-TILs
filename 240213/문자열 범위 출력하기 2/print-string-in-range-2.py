p=input()
d=int(input())
l=len(p)
for i in range(l,l-d,-1):
    print(p[i-1],end='')