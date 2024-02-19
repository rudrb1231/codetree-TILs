from sys import stdin
a, b = stdin.readline().split()

# 앞에 문자열 제거
while a[0] < '0' or a[0] > '9':
    a = a[1:]

while b[0] < '0' or b[0] > '9':
    b = b[1:]

# 앞에 수 부분 추출
num_a = ""
while a[0] >= '0' and a[0] <= '9':
    num_a += a[0]
    a = a[1:]

num_b = ""
while b[0] >= '0' and b[0] <= '9':
    num_b += b[0]
    b = b[1:]

# 출력
print(int(num_a) + int(num_b))