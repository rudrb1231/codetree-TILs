cnt=0

while True:
    n=input()
    arr=n.split()

    a=int(arr[0])
    b=int(arr[1])
    c=arr[2]

    print(a*b)

    if c=='C':
        break