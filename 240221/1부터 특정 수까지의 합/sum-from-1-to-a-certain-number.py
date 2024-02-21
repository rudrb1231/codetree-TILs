def add(a):
    b=0
    for i in range(1,a+1):
       b+=i

    return b

k=int(input())

c=add(k)

print(c//10)