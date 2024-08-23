n,r,c=map(int,input().split())
res=0

while n!=0:
    n-=1
    temp=2**n
    
    if r<temp and c<temp: #제2사분면
        res+=temp*temp*0
      
    elif r<temp and c>=temp: #제1사분면
        res+=temp*temp*1
        c-=temp

    elif r>=temp and c<temp: #제3사분면
        res+=temp*temp*2
        r-=temp
  
    else: #제4사분면
        res+=temp*temp*3
        r-=temp
        c-=temp

print(res)