x=input()


for elem in x:
    if (elem >='A'and elem <='Z') or (elem >= 'a' and elem <='z'):
        print(elem.upper(),end='')