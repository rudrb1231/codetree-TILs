count_arr = [0] * 7

# 개수 세기
arr = list(map(int, input().split()))
for elem in arr:
    count_arr[elem] += 1

# 개수 출력
for i in range(1, 7):
    cnt = count_arr[i]
    print(f"{i} - {cnt}")