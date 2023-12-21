import re
def solution(files):
    my_files=[]
    for idx,s in enumerate(files):
        #숫자 추출
        number=re.findall(r'\d+',s)
        real_number=int(number[0])
        #head추출
        head=s[:s.index(number[0])]
        head=head.lower()
        #my_file추가
        my_files.append([head,real_number,idx,s])

    #정렬
    answer=[]
    my_files.sort(key=lambda x : (x[0],x[1],x[2]))
    answer=[i[3] for i in my_files]
    return answer
