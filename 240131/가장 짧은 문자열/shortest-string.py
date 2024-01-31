a=input()
b=input()
c=input()

if len(c)>len(b) and len(b)>len(a):
    print(len(c)-len(a))
elif len(b)>len(a) and len(a)>len(c):
    print(len(b)-len(c))
elif len(a)>len(b) and len(b)>len(c):
    print(len(a)>len(c))
else:
    print(len(b)-len(a))