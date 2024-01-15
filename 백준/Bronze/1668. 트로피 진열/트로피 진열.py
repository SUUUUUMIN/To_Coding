n=int(input())
trophy=[int(input()) for _ in range(n)]
l_max,r_max=0,0
l_cnt,r_cnt=0,0
for t in trophy:
  if t>l_max:
    l_cnt+=1
    l_max=t
for t in trophy[::-1]:
  if t>r_max:
    r_cnt+=1
    r_max=t

print(l_cnt,r_cnt)