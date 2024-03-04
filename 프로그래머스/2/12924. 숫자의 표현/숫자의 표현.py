def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        temp=0
        while temp<n:
            temp+=i
            if temp==n:
                answer+=1
                break
            i+=1
    return answer