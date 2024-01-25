def solution(s):
    answer = []
    sli=s.split(' ')
    for s in sli:
        temp=''
        for j in range(len(s)):
            if j==0 and s[j].isdigit()==False:
                temp+=s[j].upper()
            elif s[j].isdigit():
                temp+=s[j]
            else:
                temp+=s[j].lower()
        answer.append(temp)
    return ' '.join(answer)