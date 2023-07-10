def solution(survey, choices):
    answer = ""
    standard = ['R','C','J','A']
    sub = ['T','F','M','N']
    for i,s in enumerate(survey):
        if s[0] not in standard:
            survey[i] = survey[i][::-1]
            choices[i] = 8-choices[i]
    choices = [i-4 for i in choices]
    score = [0]*4
    for i,s in enumerate(survey):
        if s[0] == 'R':
            score[0] += choices[i]
        elif s[0] == 'C':
            score[1] += choices[i]
        elif s[0] == 'J':
            score[2] += choices[i]
        elif s[0] == 'A':
            score[3] += choices[i]
    for i,s in enumerate(score):
        if s <= 0:
            answer += standard[i]
        else:
            answer += sub[i]
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5,3,2,7,5]
print(solution(survey,choices))