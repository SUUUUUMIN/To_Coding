import sys
input=sys.stdin.readline

#테스트 케이스
test=int(input())

for _ in range(test):
  a,b=map(int,input().split())
  #b를 수정해줍니다.
  if b%4==0:
    b=4
  else:
    b=b%4
  data=a**b
  if data%10==0:
    print(10)
  else:
    print(data%10)

##########################시간초과 코드###########################


#테스트 케이스
#test=int(input())

#반복
#for _ in range(test):
#  a,b=map(int,input().split())
#  data=a**b
#  print(data)
  #10대의 컴퓨터
 # if data%10==0: #10번 컴퓨터일 때, 10으로 출력 
 #   print(10)
 # else:
 #   print(data%10)
