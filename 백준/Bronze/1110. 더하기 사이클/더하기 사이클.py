num=int(input())
check=num
count=0
while True:
  sum=num//10+num%10
  new=num%10*10+sum%10
  num=new
  count+=1
  if(new==check):
    break
print(count)