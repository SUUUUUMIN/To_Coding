#입력받기
n,q=map(int,input().split())
music=[int(input()) for _ in range(n)]
question=[int(input()) for _ in range(q)]

#노래리스트만들기
res=[]
for i in range(n):
  for _ in range(music[i]):
    res.append(i+1)

#질문시간뽑기
for que in question:
  print(res[que])