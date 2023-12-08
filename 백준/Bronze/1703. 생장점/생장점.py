#1703

while 1:
  li=list(map(int,input().split(' ')))
  #처음 잎은 1개를 무조건 가지고 있음
  leaf=1
  
  if li[0]==0:   #0이 될 때 종료
    break

  else:
    #2개씩 for문
    for i in range(1,len(li),2):
      leaf=leaf*li[i]-li[i+1] #가지 수 * 생장점 - 가지치기
    print(leaf)