def solution(s):
    cnt=0
    i,o=0,0
    while len(s)>0:
        for idx in range(len(s)):
            if s[0]==s[idx]:
                i+=1
            else:
                o+=1
            if i==o:
                break
        cnt+=1
        s=s[idx+1:]
    return cnt