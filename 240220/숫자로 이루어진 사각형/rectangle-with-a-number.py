n=int(input())

def print_rect(a):
    t=0
    for i in range(a):
        for j in range(a):
            t+=1
            if t==10:
                t=1
            print(t,end=' ')
        print()

print_rect(n)