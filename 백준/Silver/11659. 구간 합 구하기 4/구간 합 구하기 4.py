import sys
input = sys.stdin.readline

N, Q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
s = [0]
temp = 0

for i in range(N):
    temp += a[i]
    s.append(temp)

for _ in range(Q):
    i, j = map(int, input().split(" "))
    print(s[j]-s[i-1])