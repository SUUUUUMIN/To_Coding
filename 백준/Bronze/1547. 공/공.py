#1547

#몇 번 바꿀지 입력받기
n=int(input())

#초기 컵 배열
#인덱스 일치 시키기 위해 [0,1,2,3]
cup=[0,1,2,3]

#입력받기
for i in range(n):
  x,y=map(int,input().split())
  cup[x],cup[y]=cup[y],cup[x]

#위치를 출력시키기 위해 index출력
print(cup.index(1))