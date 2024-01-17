def solution(s):
    answer=[-1]
    for i in range(1,len(s)):
        temp=s[:i]
        t=[]
        if s[i] not in temp:
            answer.append(-1)
        else:
            for j in range(len(temp)):
                if temp[j]==s[i]:
                    t.append(i-j)
            answer.append(min(t))
    return answer