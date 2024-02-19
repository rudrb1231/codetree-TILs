A=list(input())

for i in range(100):
    if A[i]=='e':
        A.pop(i)
        break
print(''.join(A))