def solution(id_list, report, k):
    answer = [0]*len(id_list)
    count={}
    re={}
    
    #초기화
    for id in id_list:
        count[id]=0
        re[id]=[]

    report=list(set(report))
    for i in range(len(report)):
        a,b=report[i].split()
        count[b]+=1
        re[a].append(b)
    li=[n for n,v in count.items() if v>=k]

    
    for name in li:
        for n,v in re.items():
            if name in v:
                answer[id_list.index(n)]+=1


    return answer