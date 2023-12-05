#시간초과 해결 -> sys.stdin.readline()
import sys
#입력받아서 합 계산하는 함수
def input_sum(num):
  s=0
  for i in range(num):
    s+=int(sys.stdin.readline())
  return s
res=[]
for i in range(3):
  num=int(sys.stdin.readline())
  s=input_sum(num)
  if s<0: #합이 음수일 때 마이너스 저장  
    res.append('-')

  elif s>0: #합이 양수일 때 플러스 저장
    res.append('+')
  
  else:    #합이 0일 때 0 저장
    res.append('0')
for i in range(3):
  print(res[i])