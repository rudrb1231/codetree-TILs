s,q=input().split()
q=int(q)
length_s=len(s)
s= list(s)

for _ in range(q):
    a,b,c = input().split()
    if a=='1':
        b,c = int(b),int(c)
        s[b-1],s[c-1]=s[c-1],s[b-1]
    else:
        for i in range(length_s):
            if s[i]==b:
                s[i]=c
    for elem in s:
        print(elem, end='')
    print()