M,D=tuple(map(int,input().split()))


def exsit_month30(M,D):
    if d<=30:
        return True
    else:
        return False


def exsit_month31(M,D):
    if M==2:
        if d<=28:
            return True
        else:
            return False
    elif