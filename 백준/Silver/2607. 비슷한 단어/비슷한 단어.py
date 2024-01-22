n=int(input())
first=list(input())
res=0
for _ in range(n-1):
  target=first[:]
  word=input()
  cnt=0
  for w in word:
    if w in target:
      target.remove(w)
    else:
      cnt+=1
  if cnt<2 and len(target)<2:
    res+=1
print(res)