from itertools import permutations
abc=list(permutations(map(int,input().split(':'))))
#print(abc)=>[(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 0), (0, 0, 1)]
cnt=0

for a,b,c in abc:
  if a>=1 and a<=12 and b<=59 and c<=59:
    cnt+=1
print(cnt)