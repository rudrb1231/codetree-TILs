A=input()
B=input()


while A.find(B) !=-1:
    start_pos = A.find(B)
    A=A[:start_pos]+A[start_pos+len(B):]

print(A)