def solution(hp):
    answer = 0
    arr=[5,3,1]
    for i in arr:
        answer+=hp//i
        hp=hp%i
        if hp==0:
            break
    return answer