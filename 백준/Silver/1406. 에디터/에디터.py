import sys
left=list(sys.stdin.readline().rstrip())
right=[]
n=int(input())
for _ in range(n):
  order=sys.stdin.readline().split()
  if order[0]=='L'and left:
     right.append(left.pop())
  elif order[0]=='D'and right:
     left.append(right.pop())
  elif order[0]=='B'and left:
     left.pop()
  elif order[0]=='P':
    left.append(order[1])
print(''.join(left+list(reversed(right))))