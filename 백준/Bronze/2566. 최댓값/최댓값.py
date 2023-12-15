#리스트 선언
arr=[list(map(int,input().split()))for _ in range(9)]


#max구현
row=col=0
val=-1 #모든 원소가 0일 수도 있음

for i in range(9):
  for j in range(9):
    if arr[i][j]>val:
      val=arr[i][j]
      col=j+1
      row=i+1

print(f'{val}\n{row} {col}')