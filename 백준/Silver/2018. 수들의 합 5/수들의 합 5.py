N = int(input())

cnt, start, end, temp = 0,0,0,0
while end <= N:
    if temp == N:
        cnt += 1
        end += 1
        temp += end
    elif temp > N:
        temp -= start
        start += 1
    else:
        end+=1
        temp+=end
print(cnt)