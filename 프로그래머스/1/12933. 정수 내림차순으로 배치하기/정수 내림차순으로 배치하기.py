def solution(n):
    answer = 0
    a=list(str(n))
    a=sorted(a,reverse=True)
    answer=int(''.join(map(str, a)))
    return answer