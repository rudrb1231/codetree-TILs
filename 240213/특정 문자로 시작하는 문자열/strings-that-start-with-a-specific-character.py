n=int(input())

b=[ input() 
for _ in range(n)]

c=input()


cnt=0

tot=0
for i in range(n):
    if b[i][0]==c:
        cnt+=1
        tot+=len(b[i])

print(cnt,end=' ')
print(f"{tot/cnt:0.2f}")