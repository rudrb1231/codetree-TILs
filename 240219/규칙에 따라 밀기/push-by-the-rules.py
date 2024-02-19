A= input()

cmd=input()

for i in cmd:
    if i=='L':
        A=A[1:]+A[0]
    else:
        A=A[-1]+A[:-1]

print(A)