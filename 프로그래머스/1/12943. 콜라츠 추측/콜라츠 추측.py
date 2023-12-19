def solution(num):
    answer = 0
    while answer<500:
        if num==1:
            break
        elif num%2==0: #짝수
            num=num/2
            answer+=1
        elif num%2==1: #홀수
            num=num*3+1
            answer+=1
    if answer==500:
        answer=-1
    return answer