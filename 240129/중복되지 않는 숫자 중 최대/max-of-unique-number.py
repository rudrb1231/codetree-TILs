dic = {}

n = int(input())

lst = list(map(int, input().split()))

for x in lst:

    if x in dic:

        dic[x] += 1

    else :

        dic[x] = 1

sortDic = sorted((dic), reverse=True)

flag = 0

for x in sortDic:

    if dic[x] > 1:
        continue
    else:
        flag = x
        break
    
print( "-1" if flag == 0 else flag)