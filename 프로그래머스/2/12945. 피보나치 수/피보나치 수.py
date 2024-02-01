def solution(n):
    pre=0
    fibo=1
    for i in range(2,n+1):
        fibo,pre=fibo+pre,fibo
    return fibo%1234567