n=int(input())
plist=list(map(int,input().split()))

computer=[0 for _ in range(100)]
refuse=0

for p in plist:
  if computer[p-1]==0:     #손님이 없는 자리인 상황, 앉았기 때문에 1로 변환
    computer[p-1]=1
  else:                    #손님이 앉아있는 상황, 거절+1
    refuse+=1
print(refuse)