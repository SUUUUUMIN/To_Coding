def solution(friends, gifts):
    answer = {f:0 for f in friends}
    history={f:{k:0 for k in friends if k!=f} for f in friends}
    present={f:0 for f in friends}
    for g in gifts:
        sender,taker=g.split()
        history[sender][taker]+=1
        present[sender]+=1
        present[taker]-=1

    for f in friends:
        for p in history[f].keys():
            if (history[f][p]!=0 or history[p][f]!=0) and history[f][p]!=history[p][f]:
                if history[f][p]<history[p][f]:
                    answer[p]+=1
                else:
                    answer[f]+=1
            else:
                if present[f]<present[p]:
                    answer[p]+=1
                elif present[f]>present[p]:
                    answer[f]+=1
                else:
                    continue
    
    return (max(answer.values())//2)