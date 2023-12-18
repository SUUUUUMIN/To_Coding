#딕셔너리
color={
    'black':[0,1],
    'brown':[1,10],
    'red':[2,100],
    'orange':[3,1000],
    'yellow':[4,10000],
    'green':[5,100000],
    'blue':[6,1000000],
    'violet':[7,10000000],
    'grey':[8,100000000],
    'white':[9,1000000000]
}

#입력받기
li=[]
for _ in range(3):
  li.append(input())

#a,b,c 쪼개기
a=color[li[0]][0]
b=color[li[1]][0]
c=color[li[2]][1]

#결과
res=(a*10+b)*c
print(res)