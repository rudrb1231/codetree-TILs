A=input().split()

def palindrome(A):
    if A[::-1]==A:
        print('Yes')
    else:
        print('No')


palindrome(A)