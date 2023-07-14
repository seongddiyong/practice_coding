def solution(lottos, win_nums):
    cnt = 0
    zeros = 0
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            zeros += 1
    
    maxi = 7 - (cnt+zeros) 
    if maxi > 6: maxi = 6 
    mini = 7 - cnt 
    if mini > 6: mini = 6 
    
    answer = [maxi,mini]
    return answer