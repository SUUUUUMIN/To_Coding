from itertools import permutations
n=int(input())
k=int(input())
card=[input() for _ in range(n)]
print(len(set(''.join(i) for i in permutations(card,k))))