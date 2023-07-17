def sol(a,b):
    return (a[1] - b[1]) / (a[0] - b[0]) 

def solution(dots):
    answer = 0
    s1 = (dots[0][0], dots[0][1])
    s2 = (dots[1][0], dots[1][1])
    s3 = (dots[2][0], dots[2][1])
    s4 = (dots[3][0], dots[3][1])
    
    if sol(s1,s2) == sol(s3,s4):
        answer = 1
    elif sol(s1,s3) == sol(s2,s4):
        answer = 1
    elif sol(s1,s4) == sol(s2,s3):
        answer = 1
        
    return answer