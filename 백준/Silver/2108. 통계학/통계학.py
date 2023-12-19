#2108
#sys
import sys
input=sys.stdin.readline
#입력받기
n=int(input())
li=[]   #숫자 입력받는 리스트
li_f={} #카운트를 위한 딕셔너리
for _ in range(n):
  num=int(input())
  li.append(num)
  if num not in li_f:
    li_f[num]=1
  else:
    li_f[num]+=1

#정렬
li.sort()

#산술평균
me=round(sum(li)/n)

#중앙값
med=li[n//2]

#최빈값
maxf=max(li_f.values())
feq_l=[k for k,v in li_f.items() if maxf==v]
feq_l.sort()
if len(feq_l)>1:
  feq=feq_l[1]
else:
  feq=feq_l[0]
  
#범위
ran=li[n-1]-li[0]

print(f'{me}\n{med}\n{feq}\n{ran}')