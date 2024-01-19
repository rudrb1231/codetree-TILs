n=int(input())
c=-1
for i in range(n):
    for j in range(n):
        x='A'
        c+=1
        print(chr(ord(x)+c),end='')
    print()