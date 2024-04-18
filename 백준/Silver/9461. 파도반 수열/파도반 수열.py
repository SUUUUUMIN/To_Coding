dp=[0]*101
dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
t=int(input())
for _ in range(t):
  n=int(input())
  for i in range(4,n):
    dp[i]=dp[i-3]+dp[i-2]
  print(dp[n-1])