A=list(input())
B=list(input())
leng=len(A)
leng2=len(B)

for i in range(leng):
    if A[i:i+leng2]==B[:]:
        A=A[:i]

print(''.join(A))