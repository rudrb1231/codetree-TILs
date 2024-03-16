A=input()
def palindrome(A):
    if A==A[::-1]:
        print('Yes')
    else:
        print('No')


palindrome(A)