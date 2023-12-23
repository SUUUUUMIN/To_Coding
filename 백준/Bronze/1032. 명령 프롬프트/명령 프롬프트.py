#1032
n=int(input())        #전체 개수
first=list(input())   #첫번째 글자
fir_len=len(first)    #글자 수

for _ in range(n-1):
  other=list(input())       #다른 글자 입력
  for i in range(fir_len):
    if first[i]!=other[i]: #글자가 다른경우
      first[i]='?'

print(''.join(first))