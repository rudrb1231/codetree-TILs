s=input()

a=s[0]
b=s[1]
for i in range(len(s)):
    if s[i]==a:
        s =s[:i]+b+s[i+1:]
    elif s[i]==b:
        s = s[:i]+a + s[i+1:]

print(s)