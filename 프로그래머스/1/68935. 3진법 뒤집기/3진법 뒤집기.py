def solution(n):
    result=''
    while n>0:
        n,mod=divmod(n,3)
        result+=str(mod)
    
    answer=int(result,3)
    return answer