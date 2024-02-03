n=int(input())
score=[0,0,0]
flag=[0,0,0]
for _ in range(n):
  a,b,c=map(int,input().split())
  flag[0]+=a**2
  flag[1]+=b**2
  flag[2]+=c**2
  score[0]+=a
  score[1]+=b
  score[2]+=c


mvalue=max(score)
if score.count(mvalue)==1:
  idx=score.index(mvalue)
  print(idx+1,score[idx])
else:
  fvalue=max(flag)
  idx=flag.index(fvalue)
  if flag.count(fvalue)==1:
    print(idx+1,score[idx])
  else:
    print(0,score[idx])