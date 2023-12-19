def solution(N, stages):
    answer = []
    fail={}
    #도전자 수
    people=len(stages)
    
    #실패율
    for i in range(1,N+1):
        if people!=0:
            cnt=stages.count(i)
            fail[i]=cnt/people
            people-=cnt
        else:
            fail[i]=0

    answer=list(fail.items())
    answer=sorted(answer,key=lambda x: (-x[1],x[0]))
    res=[answer[i][0] for i in range(len(answer))]
    return res