#입력받기
H,M=map(int,input().split())
C=int(input())

#M+C
M=M+C
if M//60>0:  #60분 이상일 때
  H=H+(M//60)
  M=M%60

if H>=24:    #자정에 시간이 바뀔 때
  H=H-24

print(H,M)