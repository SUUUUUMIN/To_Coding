
def solution(name, yearning, photo):
    answer = []
    for people in  photo:
        sum=0   #초기화
        for person in people:
            if person in name:
                idx=name.index(person)
                sum+=yearning[idx]
        answer.append(sum)
    return answer