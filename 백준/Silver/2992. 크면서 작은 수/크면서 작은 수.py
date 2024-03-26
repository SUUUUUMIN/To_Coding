from itertools import permutations
number=list(input())
num=int(''.join(number))
per=list(permutations(sorted(number),len(number)))
for p in per:
  temp=int(''.join(p))
  if temp>num:
    print(temp)
    break
else:
  print(0)