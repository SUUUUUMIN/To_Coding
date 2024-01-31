def solution(n):
    nbin=bin(n)[2:].count('1')
    other=n
    while True:
        other+=1
        obin=bin(other)[2:].count('1')
        if nbin==obin:
            return other
            break
