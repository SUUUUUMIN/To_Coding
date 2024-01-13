def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        b1=format(arr1[i],'b').rjust(n,'0')
        b2=format(arr2[i],'b').rjust(n,'0')
        
        temp=''
        for j in range(n):
            if b1[j]=='1' or b2[j]=='1':
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    
    return answer