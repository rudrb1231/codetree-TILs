cnt=0
a=[]
while True:

    p=input()
    a.append(p)
    if p=='0':
        break
    cnt+=1
    
print(cnt)

for i in range(cnt):
    if i%2==0:
        print(a[i])