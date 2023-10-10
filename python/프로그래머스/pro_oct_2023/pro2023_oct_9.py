def solution(n, left, right):
    answer = []
    temp = [i for i in range(1,n+1)]
    for i in range(left,right+1):
        a = temp[i%n]
        if a < i//n+1:
            a = i//n+1
        answer.append(a)
    return answer