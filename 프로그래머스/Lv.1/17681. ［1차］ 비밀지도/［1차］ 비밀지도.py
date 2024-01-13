def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        b1=format(arr1[i],'b')
        b2=format(arr2[i],'b')
        if len(b1)!=n:
            b1='0'*(n-len(b1))+b1
        if len(b2)!=n:
            b2='0'*(n-len(b2))+b2
        
        temp=''
        for j in range(n):
            if b1[j]=='1' or b2[j]=='1':
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    
    return answer