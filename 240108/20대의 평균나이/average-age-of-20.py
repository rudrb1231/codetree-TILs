ave=0
cnt=0
while True:
    n=int(input())

    if n>=30:
        break
    ave+=n
    cnt+=1


print(f'{ave/cnt:0.2f}')