n=int(input())
c=0

for i in range(1,101):
    c+=i
    if c>=n:
        print(i)
        break