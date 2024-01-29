#n개의 원소 
#q개의 질의 
#1 a>> a번쨰 원소 출력
#2 a>> a있는지 판단 후 있으면 원소 몇번쨰, 2개이상이면 index가 더 작은 원소 ,없으면 0출력
#3 a b >> a부터 b까지 공백 사이에 두고 출력

n,q= tuple(map(int,input().split()))
arr = list(map(int, input().split()))

for _ in range(q):

    quest = list(map(int, input().split()))

    if quest[0] ==1:
        a=quest[1]
        print(arr[a-1])

    elif quest[0] == 2:
        a=quest[1]
        idx= -1
        if a in arr:
            idx = arr.index(a)
        print(idx+1)

    else:
        a=quest[1]
        b=quest[2]
        for i in range(a-1, b):
            print(arr[i], end=' ')
        print()