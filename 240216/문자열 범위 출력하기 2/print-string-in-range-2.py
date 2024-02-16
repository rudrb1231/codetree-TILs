p=input()
d=int(input())
l=len(p)
cnt=0



for i in range(l-1,-1,-1):
    if cnt>=d:
        break
    
    print(p[i],end='')
    cnt+=1