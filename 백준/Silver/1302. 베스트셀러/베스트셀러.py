#권수
n=int(input())
books=[]
for _ in range(n):
  books.append(input())

#딕셔너리
dic={}
for book in books:
  if book not in dic:
    dic[book]=1
  else:
    dic[book]+=1

#정렬
dic_li=list(sorted(dic.items(),key=lambda x : (-x[1],x[0])))
print(dic_li[0][0])