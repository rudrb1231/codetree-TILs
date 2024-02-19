n=list(input())
length = len(n)

while length >1:

    j=int(input())
 
    if j>=length:
        n.pop(-1)
        length-=1
    else:
        n.pop(j)
        length-=1
        
    print(''.join(n))