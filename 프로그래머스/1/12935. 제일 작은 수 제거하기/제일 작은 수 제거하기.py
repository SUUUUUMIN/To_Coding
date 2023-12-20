def solution(arr):
    m=min(arr)
    a=[i for i in arr if m != i]
    if len(a)==0:
        a=[-1]
    return a