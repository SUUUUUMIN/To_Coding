key=input()
cyper=input()
l=len(cyper)//len(key)
sort_key=sorted(key)

dic={}
for i in range(len(key)):
  dic[i] = sort_key[i] + cyper[l*i:l*(i+1)]
li=list(dic.values())

res=[]
for k in key:
  for j in range(len(li)):
    if k==li[j][0]:
      res.append(li.pop(j))
      break
for i in range(1,l+1):
  for j in res:
    print(j[i],end='')