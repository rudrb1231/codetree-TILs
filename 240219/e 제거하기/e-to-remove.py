A=list(input())

idx=-1


for i in range(len(A)-2):
    if A[i]== 'e' :
        A=A[:i]+A[i+1:]
        break
print(''.join(A))