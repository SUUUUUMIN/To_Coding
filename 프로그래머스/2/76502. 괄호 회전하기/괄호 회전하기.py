def solution(s):
    answer = 0
    pair={
        ')':'(',
        '}':'{',
        ']':'['
    }
    for i in range(len(s)):
        stack=[]
        new_s=s[i:]+s[:i]
        for a in new_s:
            if a in '([{':
                stack.append(a)
            else:
                if stack and stack[-1]==pair[a]:
                    stack.pop()
                    continue
                else:
                    break
        else:
            if not stack:
                answer+=1
                    
    return answer