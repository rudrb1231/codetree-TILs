m, d = tuple(map(int, input().split()))

def exist_month30(m, d):
    if d <=28:
        return True
    else:
        return False  

def exist_month31(m, d):
	
    if m == 2:
        if d >= 29:
            return False
        else:
            return True
    if d <= 31:
        return True
    else:
        return False

ans = False


if m == 4 or m == 6 or m ==  9 or m == 11:
    ans = exist_month30(m,d)
elif m==1 or m==3 or m==2 or m==5 or m==7 or m==8 or m==12:
    ans = exist_month31(m,d)
else:
    ans= False

if ans:
    print("Yes")
else:
    print("No")