a=input()

cnt1=0
cnt2=0

for i in range(len(a)):
    if a[i:i+2]=='ee':
        cnt1+=1
    if a[i:i+2]=='eb':
        cnt2+=1
print(cnt1,cnt2)