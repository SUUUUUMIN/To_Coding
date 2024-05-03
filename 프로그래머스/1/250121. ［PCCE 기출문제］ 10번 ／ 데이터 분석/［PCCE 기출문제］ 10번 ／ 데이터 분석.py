def solution(data, ext, val_ext, sort_by):
    answer = []
    con=['code','date','maximum','remain']
    
    idx=con.index(ext)
    sdx=con.index(sort_by)
    for d in data:
        if d[idx]<val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[sdx])
    return answer