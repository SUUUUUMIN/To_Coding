King=1
Queen=1
Rook=2
Bishop=2
Knight=2
Pwan=8

K,Q,R,B,N,P=map(int,input().split())
print(f'{King-K} {Queen-Q} {Rook-R} {Bishop-B} {Knight-N} {Pwan-P}')