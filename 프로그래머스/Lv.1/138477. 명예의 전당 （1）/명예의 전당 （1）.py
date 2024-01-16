def solution(k, score):
    answer = []
    temp=[]
    for i in score:
        if len(temp)<k:
            temp.append(i)
        else:
            if min(temp)<i:
                temp.remove(min(temp))
                temp.append(i)
        answer.append(min(temp))
    return answer