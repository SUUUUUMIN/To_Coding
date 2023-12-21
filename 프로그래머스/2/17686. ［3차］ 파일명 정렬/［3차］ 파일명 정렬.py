import re
def solution(files):
    answer=[]
    dic=[]
    for file in files:
        #숫자
        idx=re.findall(r'\d+',file)
        real=int(idx[0])

        #head
        head=file[:file.index(idx[0])].lower()

        #dic채우기
        dic.append([head,real,files.index(file)])

    #정렬
    dic.sort(key=lambda x:(x[0],x[1],x[2]))

    #원본파일 출력
    for i in range(len(dic)):
        answer.append(files[dic[i][2]])
        
    return answer