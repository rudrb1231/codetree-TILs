# 변수 선언 및 입력:
n = int(input())
a = list(map(int, input().split()))
indices = list()

# 첫 번째 원소는 항상 답이 됩니다.
indices.append(0)

# 바로 직전에 답으로 추가한 원소보다
# 현재 원소가 더 큰 경우에만 답으로 추가합니다.
for i in range(1, n):
    last_idx = indices[-1]
    if a[i] > a[last_idx]:
        indices.append(i)

for idx in indices[::-1]:
    print(idx + 1, end=' ')