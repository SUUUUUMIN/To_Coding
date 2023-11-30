def solution(emergency):
    arr=sorted(emergency,reverse=True)
    answer=[]
    for i in emergency:
        answer.append(arr.index(i)+1)
    
    return answer