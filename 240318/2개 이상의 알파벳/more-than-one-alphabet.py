A=input()

def judge(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[0]:
            return True
    return False


if judge(A):
    print('Yes')
else:
    print('No')