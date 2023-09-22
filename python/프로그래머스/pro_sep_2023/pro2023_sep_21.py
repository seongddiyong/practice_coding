def solution(s):
    answer = [] 
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        newString = ''
        cnt = 1
        pattern = s[:i]
        for j in range(i,len(s)+i,i):
            if pattern == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    newString = newString + pattern
                else:
                    newString = newString + str(cnt) + pattern
                pattern = s[j:j+i]
                cnt = 1
        answer.append(len(newString))
    return min(answer)

s = "ababcdcdababcdcd"
print(solution(s))