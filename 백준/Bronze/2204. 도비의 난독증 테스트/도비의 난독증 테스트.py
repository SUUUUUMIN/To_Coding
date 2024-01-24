while True:
  n=int(input())
  if n==0:
    break
  else:
    dic={}
    for _ in range(n):
      w=input()
      dic[w]=w.lower()
    res=sorted(dic.items(),key=lambda x : x[1])
    print(res[0][0])