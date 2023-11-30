import math
def solution(n):
    tot=n*6
    total=tot//math.gcd(6,n)
    answer=total//6
    return answer