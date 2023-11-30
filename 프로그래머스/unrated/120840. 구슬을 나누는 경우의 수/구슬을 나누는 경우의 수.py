def solution(balls, share):
    answer = 0
    tmp1=1
    tmp2=1
    tmp3=1
    ch=balls-share
    for i in range(1,balls+1):
        tmp1*=i
    for j in range(1,share+1):
        tmp2*=j
    for k in range(1,ch+1):
        tmp3*=k
    answer=tmp1/(tmp2*tmp3)
    return answer