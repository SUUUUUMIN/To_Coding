from collections import deque

start,dest=map(int,input().split())

if start >= dest:
    print(start - dest)
    exit()

move = [0] * 100001
queue = deque([start])

while move[dest] == 0:
    node = queue.popleft()
    next_positions = [node - 1, node + 1, node * 2]
    for next_pos in next_positions:
        if 0 <= next_pos <= 100000 and move[next_pos] == 0:
            move[next_pos] = move[node] + 1
            queue.append(next_pos)

print(move[dest])