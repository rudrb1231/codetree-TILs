n1,n2=list(map(int,input().split()))

A=list(map(int,input().split()))

B=list(map(int,input().split()))


def is_same(n):
    for i in range(n2):
        if A[i+n] != B[i]:
            return False

    return True


def is_subsequence():
    for i in range(n1-n2+1):
        if is_same(i):
            return True

    return False


if is_subsequence():
    print("Yes")
else:
    print("No")