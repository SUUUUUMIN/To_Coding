def solution(s):
    p_n=y_n=0
    for i in s:
        if i=='p'or i=='P':
            p_n+=1
        elif i=='y' or i=='Y':
            y_n+=1
    if p_n!=y_n:
        return False
    
    return True