string = input()
length = len(string)
s_str = string[1]

for i in range(length):
    if s_str ==string[i]:
        string = string[:i] + string[0] + string[i + 1:]

print(string)