while True:
  stack=[]
  _str=input()
  flag=0
  if _str=='.' and len(_str)==1:
    break
  for s in _str:
    if s in ['(','[']:
      stack.append(s)
    elif s in [')',']']:
      if not stack: #비어있는 경우
        flag=1
        break
      elif s==')':
        if stack.pop() != '(':
          flag=1
          break
      elif s==']':
        if stack.pop() != '[':
          flag=1
          break

  if flag==0 and len(stack)==0:
    print('yes')
  else:
    print('no')