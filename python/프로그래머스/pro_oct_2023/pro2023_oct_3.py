def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i[0] == 'r':
            answer[0] += 1
        elif i[0] == 'l':
            answer[0] -= 1
        elif i[0] == 'd':
            answer[1] -= 1
        else:
            answer[1] += 1
        if answer[0] > board[0]//2:
            answer[0] = board[0]//2
        elif answer[0] < board[0]//2 * -1:
            answer[0] = board[0]//2 * -1
        elif answer[1] > board[1]//2:
            answer[1] = board[1]//2
        elif answer[1] < board[1]//2 * -1:
            answer[1] = board[1]//2 * -1
    return answer