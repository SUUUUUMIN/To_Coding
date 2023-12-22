def solution(left, right):
    number=[i for i in range(left,right+1)]
    
    for num in number:
        cnt=0
        for i in range(1,num+1):
            if num%i==0:
                cnt+=1
        if cnt%2==1:
            number[number.index(num)]=num*-1
        
    return sum(number)
    