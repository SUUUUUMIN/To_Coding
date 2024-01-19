def solution(k, m, score):
    score.sort(reverse=True)
    i=0
    answer=0
    while i+m<=len(score):
        box=score[i:i+m]
        answer+=min(box)*m
        i+=m
    return answer