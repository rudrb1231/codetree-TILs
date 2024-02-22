y=int(input())



def judge(n):
    if n<=2021:
        if n%4==0:
            return True
            if n%100==0 and n%400==0:
                return False
    return False

if judge(y):
    print('true')
else:
    print('false')