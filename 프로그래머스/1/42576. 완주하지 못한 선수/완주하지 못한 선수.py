def solution(participant, completion):
    answer={}
    for p in participant:
        if p in answer:
            answer[p]+=1
        else:
            answer[p]=1
    for c in completion:
        if c in answer.keys():
            if answer[c]==1:
                del answer[c]
            else:
                answer[c]-=1
    return list(answer.keys())[0]