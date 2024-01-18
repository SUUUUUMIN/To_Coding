def solution(nums):
    nonum=list(set(nums))
    take=len(nums)/2
    answer = take if take<len(nonum) else len(nonum)
    
    return answer