y,m,d=list(map(int,input().split()))


#윤년일때 true 아니면 false
def years(y):
    if (y%4==0 and y%100==0) and y%400==0:
        return True 
    elif y%4==0 and y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False


def month_day(y,m,d): 
    if m==4 or m==6 or m==9 or m==11: # 30일만 있는 달 31일일떄만 false#
        if d==31:
            return False
        else:
            return True
    elif m==2:
        if years(y):
            if d>29:
                return False
            else:
                return True
        else:
            if d>28:
                return False
            else:
                return True
    else:
        return True




def seasons(y,m,d):

    if month_day(y,m,d) and (m==3 or m==4 or m==5):
        print('Spring')
    elif month_day(y,m,d) and (m==6 or m==7 or m==8):
        print('Summer')
    elif month_day(y,m,d) and (m==9 or m==10 or m==11):
        print('Fall')
    elif month_day(y,m,d) and (m==12 or m==1 or m==2):
        print('Winter')
    else:
        print('-1')


years(y)

seasons(y,m,d)