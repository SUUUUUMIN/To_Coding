def find_date(date,today):
    if date[0]>today[0]:
        return True
    if date[0]==today[0] and date[1]>today[1]:
        return True
    if date[0]==today[0] and date[1]==today[1] and date[2]>today[2]:
        return True
    return False

def solution(today, terms, privacies):
    answer = []
    data={}
    today=list(map(int,today.split('.')))
    #terms 쪼개기
    for t in terms:
        a,b=t.split()
        data[a]=int(b)
    
    for i in range(len(privacies)):
        res=[]
        month=0
        date,rank=privacies[i].split()
        date=list(map(int,date.split('.')))
        
        #월 조정
        date[1]+=data[rank]
        
        if date[1]>12:
            if date[1]%12==0:
                date[0]+=date[1]//12-1
                date[1]=12
            else:
                date[0]+=date[1]//12
                date[1]%=12
                
        if not find_date(date,today):
            answer.append(i+1)
            
    return answer