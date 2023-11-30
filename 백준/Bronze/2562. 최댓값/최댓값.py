A=[]
for i in range(9):
    new=int(input())
    A.append(new)
    
print(max(A))
print(A.index(max(A))+1)