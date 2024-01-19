n=int(input())

for i in range(n):
    for j in reversed (range(i+1)):
        print(n-j,end=' ')
    print()