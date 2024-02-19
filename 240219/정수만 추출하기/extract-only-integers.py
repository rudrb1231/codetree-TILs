# 문자열을 구현하여 입력받습니다.
a, b = input().split()

idx1 = 0
idx2 = 0

# a의 정수로 변환 가능한 최대 인덱스를 찾습니다.
for elem in a:
	if elem <= '9' and elem >= '0':
		idx1 += 1
	else:
		break

# b의 정수로 변환 가능한 최대 인덱스를 찾습니다.
for elem in b:
	if elem <= '9' and elem >= '0':
		idx2 += 1
	else:
		break
	
str1 = a[:idx1]
str2 = b[:idx2]
	
# 합쳐진 문자열을 숫자로 바꿉니다.
str1 = int(str1)
str2 = int(str2)

# 두 숫자의 합을 출력합니다.
print(str1 + str2)