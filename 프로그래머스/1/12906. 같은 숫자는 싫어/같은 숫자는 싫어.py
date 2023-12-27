def solution(arr):
    answer=[]
    arr=list(arr)
    i=0
    for a in arr:
        if i==0:
            answer.append(a)
            i+=1
        else:
            if answer[i-1] != a:
                answer.append(a)
                i+=1
            else:
                pass
    return answer