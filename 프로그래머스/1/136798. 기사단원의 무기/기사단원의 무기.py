def solution(number, limit, power):
    cnt=0
    for i in range(1,number+1):
        temp=0
        for k in range(1,int(i**0.5)+1):
            if i%k==0:
                temp+=1
                if k**2 != i:
                    temp+=1
        if temp>limit:
            cnt+=power
        else:
            cnt+=temp
    return cnt