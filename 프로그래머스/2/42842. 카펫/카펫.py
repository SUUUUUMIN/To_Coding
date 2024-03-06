def solution(brown, yellow):
    ans = []
    for i in range(1,yellow+1):
        if yellow%i==0:
            x=yellow//i
            y=i
            if (x*2)+(y*2)+4==brown:
                ans.append(x+2)
                ans.append(y+2)
                break
    return ans