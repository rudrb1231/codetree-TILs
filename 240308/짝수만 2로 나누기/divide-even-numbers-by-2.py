n=int(input())

inp=list(map(int,input().split()))


for elem in inp:
    if elem%2==0:
        elem=elem//2
    print(elem,end=' ')