def magic(m):
    if m%2==0 and ((m%10)+(m//10))%5==0:
        print('Yes')
    else:
        print('No')

n=int(input())

magic(n)