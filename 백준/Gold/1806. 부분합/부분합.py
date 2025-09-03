N, S = map(int,input().split())
A = [int(x) for x in input().split()]
C = [0]
tot = 0
for num in A:
    tot += num
    C.append(tot)

start, end, temp, m = 1, 1, 0, N+1

while end <= N:
    temp = C[end]-C[start-1]
    if temp < S:
        end+=1
    else:
        m = min(m, end-start+1)
        start+=1

if m==N+1:
    print(0)
else:
    print(m)