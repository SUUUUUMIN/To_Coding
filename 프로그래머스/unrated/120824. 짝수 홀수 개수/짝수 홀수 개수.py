def solution(num_list):
    j=0
    h=0
    for i in num_list:
        if i%2==0:
            j+=1
        else:
            h+=1
    answer = [j,h]
    return answer