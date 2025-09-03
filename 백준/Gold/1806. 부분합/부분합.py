N, S = map(int,input().split())
A = [int(x) for x in input().split()]
C = [0]
tot = 0
for num in A:
    tot += num
    C.append(tot)

start, end, temp, m = 0, 1, 0, N+1

while end <= N:
    temp = C[end]-C[start]
    if temp < S:
        end+=1
    else:
        m = min(m, end-start)
        start+=1

if m==N+1:
    print(0)
else:
    print(m)