def solution(s):
    res=[]
    for i in range(1, len(s)+1): 
        b = ''
        cnt = 1 
        ch=s[:i]

        for j in range(i, len(s)+i, i): 
            if ch==s[j:i+j]:
                cnt+=1 
                
            else: 
                if cnt!=1:
                    b = b + str(cnt)+ch
                else:
                    b = b + ch
        
                ch=s[j:j+i]
                cnt = 1
        res.append(len(b))
            
    return min(res)