N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()

cnt, start, end = 0, 0, N-1

while start < end:
    if A[start]+A[end] < M:
        start += 1
    elif  A[start]+A[end] > M:
        end -= 1
    else:
        cnt+=1
        start+=1
        end-=1
print(cnt)