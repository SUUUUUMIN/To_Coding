#1837

#P,K입력받기
p,k=map(int,input().split(' '))
flag=0 # Good/Bad 판별 플래그

#P가 K로 이하 소수로 나눠지면 Bad, 서로소이면 Good
#1은 어디나 소수이니까 2부터 시작
for i in range(2,k):
  if p%i == 0:
    print("BAD",i)
    flag=1
    break #Bad면 더 할 필요 없음
#Good 판별해서 프린트
if flag==0:
  print("GOOD")