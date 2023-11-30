def solution(sides):
    sides.sort()
    l=sides[0]+sides[1]
    if sides[2]<l:
        return 1
    else:
        return 2
