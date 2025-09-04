N = int(input())
A = list(map(int,input().split()))
A.sort()
cnt = 0

for k in range(N):
    find = A[k]
    start, end = 0, N-1
    while start < end:
        if A[start] + A[end] == find:
            if start != k and end!= k:
                cnt+=1
                break
            elif start == k:
                start += 1
            elif end == k:
                end -= 1
        elif A[start]+A[end] < find:
            start += 1
        else:
            end -= 1

print(cnt)