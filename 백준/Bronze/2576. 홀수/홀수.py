#2576
#7개입력받으면서 홀수 골라내기
arr=[]
for _ in range(7):
  a=int(input())
  if a%2==1:
    arr.append(a)

#홀수 없을 때 -1 반환
if len(arr) == 0:
  print(-1)
else:
  arr.sort() #정렬
  print(sum(arr))
  print(arr[0])