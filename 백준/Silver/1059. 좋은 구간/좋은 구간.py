#입력받기
idx=int(input())
li=list(map(int,input().split()))
num=int(input())

#초기값 설정
back=front=num
res=0

#숫자 추가 후 정렬
if num in li: #리스트 속 동일한 숫자
  res=0
else:
  li.append(num)
  li.append(0)
  li.sort()
  num_idx=li.index(num)             #정렬 후 입력받은 수가 중간에 있을 때
  back=li[num_idx-1]
  front=li[num_idx+1]
  res=(num-back)*(front-num)-1
print(res)