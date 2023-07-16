def solution(s):
    answer = [0,0]
    while s != '1':
        answer[1] += s.count('0')   # 0 의 개수 추가
        s = s.replace('0','')       # 0 제거
        s = format(int(len(s)), 'b')
        answer[0] += 1
        
    return answer

s = "110010101001"
print(solution(s))