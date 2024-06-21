n=int(input())
graph={}
for i in range(n):
  root,l,r=input().split()
  l=None if l=='.' else l
  r=None if r=='.' else r
  graph[root]=[l,r]

preorder=[]
inorder=[]
postorder=[]

def tree(graph,start='A'):
  if start==None: return
  preorder.append(start)
  tree(graph,graph[start][0])
  inorder.append(start)
  tree(graph,graph[start][1])
  postorder.append(start)

tree(graph)

for a in [preorder,inorder,postorder]:
  print(''.join(a))