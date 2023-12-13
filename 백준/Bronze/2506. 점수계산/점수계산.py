#변수설정
li=[]
res=0
s=0

#입력받기
num=int(input())
li=list(map(int,input().split()))

#for문
for i in range(num):
  if li[i]==0:   #0이 나오면 s초기화
    s=0
  else:          #0이 나올 때까지 s 1씩 증가 & res에 더하기
    s+=1
    res+=s

print(res)