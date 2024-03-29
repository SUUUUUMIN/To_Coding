from collections import deque
def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    
    first=sum(queue1)
    second=sum(queue2)
    total=first+second
    cnt=0
    
    if total%2==1:
        return -1

    while queue1 and queue2:
        if total/2 == first:
            return cnt

        elif first > total/2:
            temp=queue1.popleft()
            #queue2.append(temp)
            first-=temp
            #second+=temp
            cnt+=1

        else:
            temp=queue2.popleft()
            queue1.append(temp)
            first+=temp
            #second-=temp
            cnt+=1
            
    return -1
