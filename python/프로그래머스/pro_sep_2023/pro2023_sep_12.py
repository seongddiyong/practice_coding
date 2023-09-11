def solution(command):
    next = [[0,1],[1,0],[0,-1],[-1,0]]
    x = y = r = 0
    for i in command:
        if i == "G":
            x += next[r][0]
            y += next[r][1]
        elif i == "B":
            x -= next[r][0]
            y -= next[r][1]
        elif i == "R":
            r = (r+1)%4
        elif i == "L":
            r = (r+3)%4
    return [x,y]