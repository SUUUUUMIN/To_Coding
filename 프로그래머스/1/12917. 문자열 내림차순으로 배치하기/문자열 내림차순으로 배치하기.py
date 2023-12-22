def solution(s):
    li=list(s)
    li.sort(reverse=True)
    return ''.join(li)