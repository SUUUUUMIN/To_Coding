def solution(survey, choices):
    answer = ''
    
    dic=[{'R':0,'T':0},{'C':0,'F':0},
        {'J':0,'M':0},{'A':0,'N':0}]
    
    res=[]
    for i in range(len(survey)):
        s=list(survey[i])
        c=choices[i]
        if c>4 : res.append([s[1],c-4])
        elif c<4: res.append([s[0],4-c]) 

    #print(res)
    for r,k in res:
        if r in ['R','T']:
            dic[0][r]+=k
        elif r in ['C','F']:
            dic[1][r]+=k
        elif r in ['J','M']:
            dic[2][r]+=k
        else:
            dic[3][r]+=k
    for d in dic:
        a=[k for k,v in d.items() if v==max(d.values())]
        #print(a)
        answer+=a[0]

    return answer