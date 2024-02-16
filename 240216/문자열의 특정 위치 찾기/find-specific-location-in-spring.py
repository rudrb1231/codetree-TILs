a=input()


s=a[0:-2]

if a[-1] in s:
    print(s.index(a[-1]))
else:
    print('No')