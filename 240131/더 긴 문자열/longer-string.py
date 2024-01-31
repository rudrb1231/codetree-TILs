a=input()

b=a.split()

c=b[0]
d=b[1]


if len(c)==len(d):
    print('same')
elif len(c)>len(d):
    print(c,len(c))
else:
    print(d,len(d))