def solution(n):
    case = [(1,0),(0,1),(-1,-1)]
    c = num = i = j = cnt = 0
    st = n
    answer = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    while st != 0:
        num += 1
        cnt += 1
        answer[i][j] = num
        visited[i][j] = visited[j][i] = True
        if cnt == st:
            st -= 1
            cnt =0
            c = (c+1)%3
        i += case[c][0]
        j += case[c][1]
    temp = []
    for i in answer:
        for j in i:
            if j != 0:
                temp.append(j)
    return temp

print(solution(4))
print(solution(5))
print(solution(6))