import math
def solution(slice, n):
    a,b=divmod(n,slice)
    if b!=0:
        a+=1
    return a