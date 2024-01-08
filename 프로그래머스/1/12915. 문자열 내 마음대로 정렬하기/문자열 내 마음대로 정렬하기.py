def solution(strings, n):
    alist={}
    for idx,s in enumerate(strings):
        alist[idx]=[s[n],s]
    res=list(alist.values())
    res.sort()
    answer=[]
    for i in range(len(res)):
        answer.append(res[i][1])
    return answer