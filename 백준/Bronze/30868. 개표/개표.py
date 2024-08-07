n=int(input())
for _ in range(n):
    vote=int(input())
    print("++++ "*(vote//5)+"|"*(vote%5))