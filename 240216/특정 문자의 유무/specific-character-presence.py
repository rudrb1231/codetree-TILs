a=input()

leng=len(a)
exist1 =False
exist2 = False

#print('ee'in a,end=' ')
#print('ab'in a)

for i in range(leng-1):
    if a[i:i+2] =='ee':
        exist1=True
    if a[i:i+2] =='ab':
        exist2 =True

if exist1==True:
    print('Yes',end=' ')
else:
    print('No',end=' ')

if exist2 == True:
    print('Yes')
else:
    print('No')