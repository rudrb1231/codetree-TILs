s=input()
t=input()

#  i 01234567891011

n = len(s)
idx=-1

len_t = len(t)

for i in range(n - len_t + 1):
    all_same = True
    for j in range(len_t):
        if s[i + j] != t[j]:
            all_same = False
    
    #if s[i] == t[0] and s[i + 1] == t[1] and ....
    #    s[i + len_t - 1] == t[len_t - 1]:
    if all_same == True:
        idx=i

print(idx)