def solution(dirs):
    dict = {}
    cnt = 0
    
    def forDict(x,y,nx,ny):
        flag = True
        start = str(x) + str(y)
        end = str(nx) + str(ny)
        if start not in dict:
            dict[start] = [end]
        elif end not in dict[start]:
            dict[start].append(end)
        else: flag = False
        if end not in dict:
            dict[end] = [start]
        elif start not in dict[end]:
            dict[end].append(start)
        else: flag = False
        return flag

    xs = ys = xn = yn = 0
    for i in dirs:
        if i == "U":
            yn = ys + 1
        elif i == "R":
            xn = xs + 1
        elif i == "D":
            yn = ys - 1
        else:
            xn = xs - 1
        if -5 <= xn <= 5 and -5 <= yn <= 5:
            if forDict(xs,ys,xn,yn):
                cnt += 1
            xs = xn
            ys = yn
        else:
            if xn > 5: xn = 5
            elif xn < -5: xn = -5
            elif yn > 5: yn = 5
            elif yn < -5: yn = -5

        
    answer = cnt
    return answer


print(solution("LULLLLLLU"))