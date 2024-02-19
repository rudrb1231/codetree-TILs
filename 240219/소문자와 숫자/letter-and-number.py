x=input()


for elem in x:
    if (elem >='A'and elem <='Z') or (elem >= 'a' and elem <='z')or (elem >='1' and elem <='9'):
        print(elem.lower(),end='')