def solution(rsp):
    answer = ''
    arr={'2':'0','0':'5','5':'2'}
    for i in rsp:
        answer+=arr[i]
    return answer