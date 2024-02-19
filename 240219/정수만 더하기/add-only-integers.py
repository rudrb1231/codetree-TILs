x=input()

sum_v=0
for elem in x:
    if (elem>='0' and elem <='9'):
        d=int(elem)
        sum_v+=d

print(sum_v)