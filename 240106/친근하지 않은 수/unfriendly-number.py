inp=int(input())
n=0

for i in range(1,inp):
    if i%2==0 and i%3==0 or i%5==0:
        n+=1
print(n)