n=int(input())
cnt=0
for _ in range(n):
    temp=input()
    stack=[]
    for i in range(len(temp)):
        if stack:
            if temp[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(temp[i])
        else:
            stack.append(temp[i])
    if not stack:
        cnt+=1
print(cnt)