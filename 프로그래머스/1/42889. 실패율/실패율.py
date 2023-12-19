def solution(N, stages):
    answer = []
    cnt=[]
    fail={}
    for i in range(1,N+1):
        if i in stages:
            cnt.append(stages.count(i))
        else:
            cnt.append(0)
    people=len(stages)
    for i in range(N):
        fail[i+1]=cnt[i]/people
        people-=cnt[i]
    
    answer=list(fail.items())
    sorted(answer,key=lambda x : (x[1],-x[0]))
    
    return answer