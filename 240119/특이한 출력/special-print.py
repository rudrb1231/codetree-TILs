n=int(input())


for i in range(1,n+1):
    for j in range(1,n+1):
        c=i+j
        if c%4==0:
            print(f"({i}, {j})",end='\n')
        else:
            print(f"({i}, {j})",end=' ')