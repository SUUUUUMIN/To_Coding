def solution(x):
    n=list(map(int,str(x)))
    if x%sum(n)==0:
        return True
    else:
        return False