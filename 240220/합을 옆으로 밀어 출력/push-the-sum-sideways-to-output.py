n=int(input())
d=0
for i in range(n):
    k=int(input())
    d+=k
d=str(d)

print(d[1:]+d[0])