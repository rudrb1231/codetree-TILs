inp=int(input())
n=0

for i in range(1,inp+1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    n+=1
   
print(n)