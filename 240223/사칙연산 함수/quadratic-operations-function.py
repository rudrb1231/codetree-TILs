def calcul (a,b,c):
    if b=='+':
        print(f'{a} + {c} = {a+c}')
    elif b=='-':
        print(f'{a} - {c} = {a-c}')
    elif b=='*':
        print(f'{a} * {c} = {a*c}')
    elif b=='/':
        print(f'{a} / {c} = {a+c}')
    else:
        print('false')

inp=input().split()
a=int(inp[0])
b=inp[1]
c=int(inp[2])

calcul(a,b,c)