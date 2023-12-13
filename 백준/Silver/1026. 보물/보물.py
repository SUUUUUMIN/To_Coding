#입력받기
num=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#계산
s=0
for i in range(num):
  s+=min(a)*max(b)        #a의 최소*b의 최대
  a.pop(a.index(min(a)))  #a : pop
  b.pop(b.index(max(b)))  #b : pop
print(s)