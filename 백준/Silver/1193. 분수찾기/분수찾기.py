num=int(input())
line=1
while num>line:
  num-=line
  line+=1
# 4 => num=1, line=3
#짝수줄 경우 => 분모 1 감소, 분자 1 증가
if line%2==0:
  a=num
  b=line-num+1
#홀수줄 경우 => 분모 1 증가, 분자 1 감소
else:
  a=line-num+1
  b=num
print(f'{a}/{b}')