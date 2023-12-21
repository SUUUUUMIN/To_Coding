def solution(n):
    answer = ''
    if n%2==0:  #짝수
        answer='수박'*(n//2)
    else:       #홀수
        answer='수박'*(n//2)
        answer+='수'
    return answer