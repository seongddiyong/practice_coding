def solution(input_string):
    answer = ''
    string = list(set(input_string))
    dict = {}
    for i in string:
        cntString = input_string.count(i)
        if cntString > 1:
            dict[i] = cntString
            answer += i
    if len(answer) == 0:
        return 'N'
    for i in string:
        temp = ''
        if i in dict:
            for _ in range(dict[i]):
                temp += i
            if temp in input_string:
                input_string = input_string.replace(temp,".")
                answer = answer.replace(i,'')
    return ''.join(sorted(answer)) if len(answer) > 0 else "N"

print(solution("edeaaabbccd"))