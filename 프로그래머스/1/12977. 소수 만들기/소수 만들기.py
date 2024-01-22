from itertools import combinations
def Is_Prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
    return True

def solution(nums):
    answer=0
    num=list(combinations(nums,3))
    for a in num:
        if Is_Prime(sum(a)):
            answer+=1
    return answer