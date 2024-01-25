arr=list(map(int,input().split()))


for elem in arr:
    if elem%2==0:
        elem = elem//2
    else:
        elem = elem+3
    if elem==0:
        break

    print(elem, end=' ')