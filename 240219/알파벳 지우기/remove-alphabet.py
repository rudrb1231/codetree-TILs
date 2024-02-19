a=input()
b=input()
sum_1=''
sum_2=''
for elem in a:
    if elem >='0' and elem <='9':
        sum_1 +=elem
sum_1=int(sum_1)

for elem in b:
    if elem >='0' and elem <='9':
        sum_2 +=elem
sum_2=int(sum_2)

sum_3=sum_1+sum_2

print(sum_3)