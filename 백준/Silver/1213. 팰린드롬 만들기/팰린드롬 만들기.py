line=list(input())
dic={}
for l in line:
  if l in dic:
    dic[l]+=1
  else:
    dic[l]=1

cnt=0
mid=''
for k,v in dic.items():
  if v%2==1:
    cnt+=1
    mid=k
  if cnt>1:
    print("I'm Sorry Hansoo")
    exit()
p=''
for k,v in sorted(dic.items()):
  p+=k*(v//2)
print(p+mid+p[::-1])