import heapq
n = int(input())
dasom=int(input())
hq = []
for i in range(n-1):
    vote = int(input())
    heapq.heappush(hq, -vote)
cnt = 0
while hq:
    vote = -heapq.heappop(hq)
    if vote < dasom:
        break
    dasom += 1
    cnt += 1
    heapq.heappush(hq, -(vote - 1))
print(cnt)