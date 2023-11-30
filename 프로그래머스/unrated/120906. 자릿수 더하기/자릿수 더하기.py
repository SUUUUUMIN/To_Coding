def solution(n):
    answer = 0
    for i in range(n):
        answer+=n%10
        n=n//10
    return answer