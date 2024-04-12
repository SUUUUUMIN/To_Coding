from datetime import datetime
import math
def solution(fees, records):
    answer = [] 
    parking={} #입출차 관리하는 딕셔너리
    car={} #자동차 번호별로 시간 누적하는 딕셔너리
    
    for record in records:
        hour,num,state=record.split()
        if state=='IN': #입차
            parking[num]=datetime.strptime(hour,'%H:%M') #차번호를 key로 시간을 value
        else: #출차
            minute=datetime.strptime(hour,'%H:%M')-parking[num] #출차시간에서 입차시간 빼기
            
            #분을 기준으로 누적하기 위해 minute을 second로 바꾸고 60으로 나누기
            if num in car:
                car[num]+=minute.seconds//60
            else:
                car[num]=minute.seconds//60
            
            del parking[num] #출차하면 parking에서 삭제
    
    
    if parking: #만약 출차가 찍히지 않은 차가 있다면 23시 59분에 출차했다고 가정하기
        for num,time in parking.items():
            minute=datetime.strptime('23:59','%H:%M')-time
            if num in car:
                car[num]+=minute.seconds//60
            else:
                car[num]=minute.seconds//60

##### 누적시간을 활용해서 요금 계산하기
    for a,b in sorted(car.items()):
        if b<fees[0]:
            answer.append(fees[1])
        else:
            temp=math.ceil((b-fees[0])/fees[2])
            answer.append(fees[1]+temp*fees[3])

    return answer