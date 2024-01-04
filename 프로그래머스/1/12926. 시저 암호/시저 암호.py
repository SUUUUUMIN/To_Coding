def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            if ord(i)+n<91:
                answer+=chr(ord(i)+n)
            else:
                answer+=chr(ord(i)-26+n)
        elif i.islower():
            if ord(i)+n<123:
                answer+=chr(ord(i)+n)
            else:
                answer+=chr(ord(i)-26+n)
        else:
            answer+=' '
    return answer