#2490

#배(0) 등(1)
#3번
a=[]
for _ in range(3):
  a=list(map(int,input().split(' ')))
  a_sum=sum(a)
  if a_sum==4:    #등이 4개
    print('E')
  elif a_sum==3:  #등3 배1
    print('A')
  elif a_sum==2:  #등2 배2
    print('B')
  elif a_sum==1:  #등1 배3
    print('C')
  else:           #배4
    print('D')