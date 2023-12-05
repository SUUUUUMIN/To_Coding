def solution(numbers, hand):
    
    #시작위치
    left=[3,0]
    right=[3,2]
    
    #규칙
    rule={
        1:[0,0],
        2:[0,1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1]
    }
    
    #변수설정
    answer=''
    
    #롤링
    for num in numbers:
        if num==1 or num==4 or num==7: #1,4,7은 왼손
            answer+='L' # L저장
            left=rule[num] # 좌표 옮기기
        elif num==3 or num==6 or num==9: #3,6,9는 오른손
            answer+='R' # R저장
            right=rule[num] #좌표 옮기기
        else: #2,5,8,0=>center
            center=rule[num] #center 좌표
            
            #거리 계산
            ltoc=abs(left[0]-center[0])+abs(left[1]-center[1])
            rtoc=abs(right[0]-center[0])+abs(right[1]-center[1])
            
            #왼손이 더 가까울 때
            if ltoc < rtoc:
                answer+='L'
                left=center
            #오른손이 더 가까울 때
            elif ltoc > rtoc:
                answer+='R'
                right=center
            #거리가 동일할 때
            else:
                if hand=='right':
                    answer+='R'
                    right=center
                else:
                    answer+='L'
                    left=center
    return answer