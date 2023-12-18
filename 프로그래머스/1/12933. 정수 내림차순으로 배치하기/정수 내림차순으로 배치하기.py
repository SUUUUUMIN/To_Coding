def solution(n):
    answer = 0
    a=list(str(n))
    a=sorted(a,reverse=True)
    a_s=''.join(map(str, a))
    answer=int(a_s)
    return answer