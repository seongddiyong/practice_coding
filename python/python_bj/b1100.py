temp = [input() for _ in range(8)]
flag = 0
answer = 0
for i in temp:
    if flag == 0:
        cnt = 0
        for j in i:
            if cnt%2 == 0 and j == 'F':
                answer += 1
            cnt += 1
        flag = 1
    elif flag == 1:
        cnt = 0
        for j in i:
            if cnt%2 == 1 and j == 'F':
                answer += 1
            cnt += 1
        flag = 0
print(answer)