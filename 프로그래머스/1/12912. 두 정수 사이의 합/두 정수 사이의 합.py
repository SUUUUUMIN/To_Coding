def solution(a, b):
    #대소관계
    a,b=min(a,b),max(a,b)+1
    s=0
    for i in range(a,b):
        s+=i
    
    return s