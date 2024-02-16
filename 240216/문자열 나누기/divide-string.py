n=input()

b=input()

c=''
cnt=0
for elem in b:
    if elem !=" ":
        c+=elem

for elem in c:
    if cnt!=5:
        cnt+=1
        print(elem,end='')
    if cnt==5:
        cnt=0
        print()