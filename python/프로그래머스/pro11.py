def solution(board, moves):
    answer = 0
    bascket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bascket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(bascket) >= 2 and bascket[-1] == bascket[-2]:
            bascket = bascket[:-2]
            answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))