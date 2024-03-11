n,m=map(int,input().split())
dna=[list(input()) for _ in range(n)]
result=''
cnt=0
for i in range(m):
    dic={}
    for j in range(n):
        if dna[j][i] in dic:
            dic[dna[j][i]]+=1
        else:
            dic[dna[j][i]]=1
    idx=[k for k,v in dic.items() if max(dic.values())==v]
    if len(idx)>1:
        idx.sort()
    result+=idx[0]
    val=max(list(dic.values()))
    cnt+=(n-val)
print(f'{result}\n{cnt}')