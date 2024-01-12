def solution(food):
    temp=''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            temp+=str(i)
    answer=temp+'0'+temp[::-1]
    return answer