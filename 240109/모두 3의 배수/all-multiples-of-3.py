sat=False



for i in range(1,6):
    n=int(input())
    if n%3 !=0:
        sat=True


if sat==False:
    print('1')
else:
    print('0')