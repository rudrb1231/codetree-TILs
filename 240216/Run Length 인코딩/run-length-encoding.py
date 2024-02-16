A=input()
encoded=""

curr_char=A[0]
num_char=1

for traget_char in A[1:]:
    if traget_char == curr_char:
        num_char+=1

    else:
        encoded+=curr_char
        encoded+=str(num_char)

        curr_char = traget_char
        num_char =1

encoded += curr_char
encoded += str(num_char)

print(len(encoded))
print(encoded)