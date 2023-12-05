def solution(n):
    answer = []
    k=2
    while k<=n:
        if n%k==0:
            answer.append(k)
            n=n/k
        else:
            k+=1
    answer=list(set(answer))
    answer.sort()
    return answer