import math
def solution(line):
    answer = []
    max_x, min_x, max_y, min_y = -99999,99999,-99999,99999
    for i in range(len(line)-1):
        A,B,E = line[i]
        for j in range(i,len(line)):
            C,D,F = line[j]
            if A*D - B*C == 0:
                continue
            else:
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)
                if x % 1 != 0 or y % 1 != 0:
                    continue
                answer.append([int(x),int(y)])
                max_x = math.ceil(max(max_x,x))
                min_x = math.floor(min(min_x,x))
                max_y = math.ceil(max(max_y,y))
                min_y = math.floor(min(min_y,y))
    mapp = ['.' * (max_x - min_x+1)] * (max_y - min_y+1)
    for i,j in answer:
        mapp[j-1-min_y][i-1-min_x].replace('.','*')
        
    return mapp

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))