def solution(clothes):
    closet = {}
    for name, item in clothes:
        closet[item] = closet.get(item, 0)+1
    
    res = 1
    for v in closet.values():
        res *= (v+1)
    return res-1