import sys
input = sys.stdin.readline

n = int(input())

# RGB 중 하나로 칠했을 때의 비용을 저장하는 리스트
cost = [list(map(int, input().split())) for _ in range(n)]

# 전에 칠한 색을 제외한 가장 작은 값들을 계속해서 더하며 저장한다.
# 그 뒤에 그 중 가장 작은 값을 출력하면 된다.
for i in range(1,n):
    # 전에 칠한 색이 RED
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    # 전에 칠한 색이 GREEN
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    # 전에 칠한 색이 BLUE
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))