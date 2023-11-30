two_d = [list(map(int, input())) for _ in range(2)]
sum1=0 
sum2=0 
sum3=0

for j in range(2):
      two_d[j][0]=two_d[j][0]*100
      two_d[j][1]=two_d[j][1]*10

for i in range(3):
  sum1+=two_d[0][i]*two_d[1][2]
  sum2+=two_d[0][i]*two_d[1][1]
  sum3+=two_d[0][i]*two_d[1][0]

res=sum1+sum2+sum3
print(sum1)
print(sum2//10)
print(sum3//100)
print(res)