#2455
#필요한 변수 설정
people=0
result=0
#4개의 역을 지남
for i in range(4):
  take,pick=map(int,input().split(' '))
  people+=pick-take
  #최댓값을 뽑기 위해 result와 비교
  if result < people:
    result=people
print(result)