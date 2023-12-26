a,b = input().split()         #문자열로 입력받기

s=sum(list(map(int,a)))       #a를 리스트로 변환한 후 먼저 원소들 sum 해주기

res=0
for i in range(len(b)):       #for문 돌면서 s와 b 원소를 곱해주기
  res+=s*int(b[i])

print(res)