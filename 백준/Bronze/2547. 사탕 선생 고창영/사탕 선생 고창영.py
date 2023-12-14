#test case
t_num=int(input())

#테스트
for _ in range(t_num):
  temp=input()         #공백잡아먹는 애
  num=int(input())
  li=[]
  for _ in range(num):
    li.append(int(input()))
  
  if sum(li)%num==0:
    print('YES')
  else:
    print('NO')