#1672
dic={
    'AA':'A','AG':'C','AC':'A','AT':'G',
    'GG':'G','CG':'T','GT':'A',
    'CC':'C','CT':'G',
    'TT':'T'
}
n=int(input())
dna=list(input())
for i in range(n-2,-1,-1):
  s=''.join(sorted(dna[-2:]))
  dna[i]=dic[s]
  del dna[i+1]

print(*dna)