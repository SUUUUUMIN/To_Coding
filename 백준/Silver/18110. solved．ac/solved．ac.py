import sys
input=sys.stdin.readline
def my_round(val):
  if val-int(val)>=0.5:
    return int(val+1)
  else:
    return int(val)

n=int(input())
if n:
  cut=my_round(n*0.15)
  score=sorted(list(int(input()) for _ in range(n)))
  avg=score[cut:-cut]
  if cut>0:
    print(my_round(sum(score[cut:-cut])/len(score[cut:-cut])))
  else:
    print(my_round(sum(score)/len(score)))
else:
  print(0)