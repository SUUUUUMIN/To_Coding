def solution(price, money, count):
    new=0
    for i in range(1,count+1):
        new+=price*i
    
    if new<money:
        answer=0
    else:
        answer=new-money

    return answer