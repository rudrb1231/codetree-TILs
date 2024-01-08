cnt=0

while True:
    o=int(input())

    if o%2==1:
        continue

    print(o//2)
    cnt += 1

    if cnt>=3:
        break