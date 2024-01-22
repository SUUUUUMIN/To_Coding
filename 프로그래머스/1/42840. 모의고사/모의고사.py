def solution(answers):
    cnt=[0 for _ in range(3)]
    stu1=[1,2,3,4,5]
    stu2=[2,1,2,3,2,4,2,5]
    stu3=[3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        a=answers[i]
        if stu1[i%len(stu1)]==a:
            cnt[0]+=1
        if stu2[i%len(stu2)]==a:
            cnt[1]+=1
        if stu3[i%len(stu3)]==a:
            cnt[2]+=1
    answer=[]
    for j in range(3):
        if cnt[j]==max(cnt):
            answer.append(j+1)
    return answer