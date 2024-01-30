def solution(s):
    open=[]
    
    for i in s:
        if i=='(':
            open.append('(')
        else:
            if open==[]:
                return False
                break
            open.pop()
    if open:
        return False
    return True