n=int(input())

inp=list(map(int,input().split()))


def absolute(inp):
    for i in range(n):
        if inp[i] <0:
            inp[i]=-inp[i]
    return


absolute(inp)

for elem in inp:
    print(elem,end=' ')