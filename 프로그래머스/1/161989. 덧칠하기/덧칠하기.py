def solution(n, m, section):
    cnt=k=0
    for s in section:
        if s>k:
            cnt+=1
            k=m+s-1
    return cnt