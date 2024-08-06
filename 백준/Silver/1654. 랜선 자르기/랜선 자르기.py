import sys
input=sys.stdin.readline
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

low, high = 1, max(lan)
while low <= high:
    mid = (low + high) // 2
    temp_sum = 0
    for i in lan:  # mid 길이만큼 랜선 케이블들을 조각냄
        temp_sum += i // mid

    if temp_sum >= n:  # 랜선의 개수가 n이상이면
        low = mid + 1
    else:  # 랜선의 개수가 n미만이면
        high = mid - 1

print(high)