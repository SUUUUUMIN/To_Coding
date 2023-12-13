def solution(x, n):
    answer = []
    s=x
    for _ in range(n):
        answer.append(x)
        x+=s
        
    return answer