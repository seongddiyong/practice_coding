def solution(numbers, hand):
    answer = ''
    left = [1,4,7,10]
    right = [3,6,9,11]
    middle = [2,5,8,0]
    lnow = 10
    rnow = 11
    dict = {
        1:[1,1], 4:[2,1], 7:[3,1], 10:[4,1],
        2:[1,2], 5:[2,2], 8:[3,2], 0:[4,2],
        3:[1,1], 6:[2,1], 9:[3,1], 11:[4,1]
    }
    for num in numbers:
        if num in left:
            answer += 'L'
            lnow = num
        elif num in right:
            answer += 'R'
            rnow = num
        else:
            xl,yl = dict[lnow]
            xr,yr = dict[rnow]
            x,y = dict[num]
            dis_l = abs(xl-x) + abs(yl-y)
            dis_r = abs(xr-x) + abs(yr-y)
            if dis_l == dis_r:
                if hand == 'left':
                    answer += 'L'
                    lnow = num
                else:
                    answer += 'R'
                    rnow = num
            else:
                if dis_l < dis_r:
                    answer += 'L'
                    lnow = num
                else:
                    answer += 'R'
                    rnow = num
            
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')