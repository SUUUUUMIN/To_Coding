#from collections import deque
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in numbers[:-1]:
            answer.append(i)
    else:
        for i in numbers[1:]:
            answer.append(i)
        answer.append(numbers[0])
    
    #deque사용
    #num=deque(numbers)
    #if direction == 'right':
    #   num.rotate(1)
    #else:
    #   num.rotate(-1)
    #return list(num)
    return answer