def solution(clothes):
    answer = 0
    dic={}
    for n,t in clothes:
        if t in dic:
            dic[t]+=1
        else:
            dic[t]=1
    res=1
    for v in dic.values():
        res*=(v+1)
    return res-1