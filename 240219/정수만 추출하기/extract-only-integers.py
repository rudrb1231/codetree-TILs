x=input().split()
x1,x2=x[0],x[1]
d=0
while x1[0]<'0' or x1[0]>'9':
    x1=x1[1:]

while x2[0]<'0' or x2[0]>'9':
    x2=x2[1:]

num_a = ""
while x1[0] >= '0' and x1[0] <= '9':
    num_a += x1[0]
    x1 = x1[1:]

num_b = ""
while x2[0] >= '0' and x2[0] <= '9':
    num_b += x2[0]
    x2 = x2[1:]

# 출력
print(int(num_a) + int(num_b))