import sys

n=int(input())
arr=list(map(int,input().split()))

min_val= sys.maxsize
cnt = 0
for elem in arr:
    if min_val >elem:
        min_val = elem


for elem in arr:
    if min_val==elem:
        cnt+=1
        
print(min_val, cnt)