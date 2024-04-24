n=int(input())
li=list(map(int,input().split()))
s_li=sorted(list(set(li)))
dic={s_li[i]:i for i in range(len(s_li))}
for l in li:
  print(dic[l],end=' ')