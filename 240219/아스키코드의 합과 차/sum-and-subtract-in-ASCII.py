a=input().split()

b=ord(a[0])
c=ord(a[1])
d=0
if c>b:
    d=c-b
else:
    d=b-c
print(b+c,d)