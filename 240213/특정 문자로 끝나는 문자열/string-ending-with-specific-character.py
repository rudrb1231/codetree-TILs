string=[input() for _ in range(10)]
word=input()

cnt=0


for i in range(10):
    leng=len(string[i])
    if string[i][leng-1] == word:
        print(string[i])
        cnt+=1

if cnt==0:
    print('None')