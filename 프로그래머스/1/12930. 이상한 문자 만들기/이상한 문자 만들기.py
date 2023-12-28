def solution(s):
    word=s.split(' ')
    res=[]
    for w in word:
        answer=''
        for i in range(len(w)):
            if i%2==0:
                answer+=w[i].upper()
            else:
                answer+=w[i].lower()
        res.append(answer)
    return ' '.join(res)