#1010
#math라이브러리
import math

#반복횟수
rep=int(input())

for _ in range(rep):

  #n,r입력받기
  n,r=map(int,input().split())

  #nPr
  res=math.factorial(r)//(math.factorial(n)*math.factorial(r-n))
  print(res)