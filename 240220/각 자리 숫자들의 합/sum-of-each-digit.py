a=int(input())
cnt=0


a_str=str(a)

for elem in a_str:
    cnt+= ord(elem) - ord('0')

print(cnt)