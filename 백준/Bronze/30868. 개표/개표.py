n=int(input())
for _ in range(n):
  vote=int(input())
  point='++++ '*(vote//5)+'|'*(vote%5)
  print(point)