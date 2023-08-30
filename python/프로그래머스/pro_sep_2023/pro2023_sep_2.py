
def solution(line):
    answer = []
    for i in range(len(line)):
        A,B,E = line[i]
        for j in range(i+1,len(line)):
            C,D,F = line[j]
            if A*D - B*C == 0:
                continue
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            if x % 1 != 0 or y % 1 != 0:
                continue
            answer.append([int(x),int(y)])
            max_x = max(answer)[0]
            min_x = min(answer)[0]
            max_y = max(answer, key=lambda x: x[1])[1]
            min_y = min(answer, key=lambda x: x[1])[1]
    mapp = [['.'] * (max_x - min_x+1) for _ in range((max_y - min_y+1))]
    for s in answer:
        a,b = s
        x,y = abs(max_y-b) , abs(min_x-a)
        mapp[x][y] = '*'
    for i,v in enumerate(mapp):
        mapp[i] = ''.join(v)
    return mapp

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))