#딕셔너리
way={
 'R':[1,0],
 'L':[-1,0],
 'B':[0,-1],
 'T':[0,1],
 'RT':[1,1],
 'LT':[-1,1],
 'RB':[1,-1],
 'LB':[-1,-1]
}

#입력받고 현재 위치 좌표만들기
king,stone,N=input().split()
k=[ord(king[0])-65,int(king[1])-1]  #0,0에서 시작, 아스키코드 A=65
s=[ord(stone[0])-65,int(stone[1])-1]

#경로입력받기
li=[]
for _ in range(int(N)):
  li.append(input())

#경로 돌기
x=y=0

for path in li:
  x=k[0]+way[path][0]
  y=k[1]+way[path][1]
  if x<0 or x>7 or y<0 or y>7:  #체스판을 벗어났을 경우
    pass
  elif x==s[0] and y==s[1]:     #돌을 만났을 경우
    s_x=s[0]+way[path][0]
    s_y=s[1]+way[path][1]     
    if s_x<0 or s_x>7 or s_y<0 or s_y>7: #돌이 체스판을 벗어났을 경우
      pass
    else:
      s=[s_x,s_y]
      k=[x,y]
  else:
    k=[x,y]

#좌표 다시 돌리기
king=[chr(k[0]+65),str(k[1]+1)]
stone=[chr(s[0]+65),str(s[1]+1)]
print(''.join(king))
print(''.join(stone))