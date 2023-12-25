#입력받기
name = list(input())
n = int(input())
board = {}

for _ in range(n):
    team = input().strip()
    nowS = 1
    scores = []

    for item in ['L', 'O', 'V', 'E']:
        scores.append(team.count(item) +name.count(item))

    for i in range(len(scores)):
        for j in range(i+1, len(scores)):
            nowS *= (scores[i] + scores[j])

    board[team] = nowS % 100

#딕셔너리->리스트, 정렬
s_li=list(board.items())
s_li.sort(key=lambda x : (-x[1],x[0]))
print(s_li[0][0])
