def solution(n):
    answer = 0
    li=[]
    li=list(str(n))
    for i in range(len(li)):
        answer+=int(li[i])
    return answer