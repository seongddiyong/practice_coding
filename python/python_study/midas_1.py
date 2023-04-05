import heapq
inf = int(1e9)

def solution(M, S, D):
    n = len(M) # 지도의 세로 길이
    m = len(M[0]) # 지도의 가로 길이

    dist = [[inf]*m for _ in range(n)] # 최단 거리를 저장할 2차원 리스트, 무한대로 초기화
    dist[S[1]][S[0]] = 0 # 시작점의 최단 거리를 0으로 설정
    
    count = [[0]*m for _ in range(n)] # 최단 거리로 갈 수 있는 경로의 수를 저장할 2차원 리스트, 0으로 초기화
    count[S[1]][S[0]] = 1 # 시작점으로 가는 경로의 수는 1개
    
    heap = [] # 우선순위 큐, (최단 거리, y좌표, x좌표)를 저장
    heapq.heappush(heap, (0, S[1], S[0])) # 시작점을 우선순위 큐에 삽입

    up, down, left, right = 0,0,0,0

    while heap:
        cur_dist, cur_y, cur_x = heapq.heappop(heap) # 우선순위 큐에서 최단 거리를 갖는 지점을 꺼냄

        if cur_dist > dist[cur_y][cur_x]: # 꺼낸 지점의 최단 거리가 이미 계산된 거리보다 크다면 무시함
            continue

        if cur_y == D[1] and cur_x == D[0]: # 도착점에 도달한 경우, 최단 거리와 경로의 수를 반환함
            # return count[D[1]][D[0]]
            # a = print(f"{round(up/2)}/{round(down/2)}/{round(left/2)}/{round(right/2)}")
            a = print(f"{up/2}/{down/2}/{left/2}/{right/2}")
            return a

        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]: # 상하좌우 이동
            next_y = cur_y + dy
            next_x = cur_x + dx

            if not (0 <= next_y < n and 0 <= next_x < m) or M[next_y][next_x] == 1: # 지도를 벗어나거나 장애물이 있는 경우, 무시함
                continue

            if cur_dist+1 < dist[next_y][next_x]: # 새로운 지점으로 가는 거리가 더 짧은 경우, 최단 거리와 경로의 수를 업데이트하고 우선순위 큐에 추가함
                match dy, dx:
                    case (-1,0): down += 1
                    case (1,0): up += 1
                    case (0,-1): left += 1
                    case (0,1): right += 1
                dist[next_y][next_x] = cur_dist+1
                count[next_y][next_x] = count[cur_y][cur_x]
                heapq.heappush(heap, (dist[next_y][next_x], next_y, next_x))
            
                        
            elif cur_dist+1 == dist[next_y][next_x]: # 새로운 지점으로 가는 거리가 같은 경우, 경로의 수를 더해줌
                count[next_y][next_x] += count[cur_y][cur_x]

    return -1

M = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]
S = [0, 0]
D = [2, 2]
solution(M, S, D)