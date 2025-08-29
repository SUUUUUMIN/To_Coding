def solution(participant, completion):
    temp = {}
    for p in participant:
        if p in temp:
            temp[p]+=1
        else:
            temp[p]=1
    
    for c in completion:
        temp[c]-=1
    
    for name, val in temp.items():
        if val == 1:
            return name