def solution(my_string):
    answer = 0
    l='123456789'
    for i in my_string:
        if i in l:
            answer+=int(i)
    return answer