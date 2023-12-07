# 숫자 입력받기
a,b=map(int,input().split())

#좌표로 변환
#세로로 4칸씩 -> 4의 배수 유의
#가로 : 몫 , 세로 : 나머지
# 4의 배수이면 [몫-1 ,4]
x=[(a//4)-1 if a%4==0 else a//4,4 if a%4==0 else a%4]
y=[(b//4)-1 if b%4==0 else b//4,4 if b%4==0 else b%4]

#거리 구하기
dis = abs(x[0]-y[0])+abs(x[1]-y[1])
print(dis)