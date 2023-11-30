A=[]
for i in range(10):
    new=int(input())
    A.append(new%42)

A=set(A)
print(len(A))