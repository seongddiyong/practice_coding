def temp(a,b):
    return not (a[1] < b[0] or b[1] < a[0] or a[3] < b[2] or b[3] < a[2])
    # 0,1 : x / 2,3 : y

def solution(n, x1, y1, x2, y2):
    graph = [[] for _ in range(n)]

    spot = [(min(x1[i],x2[i]), max(x1[i],x2[i]), min(y1[i],y2[i]), max(y1[i],y2[i])) for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
        
            if temp(spot[i],spot[j]):
                graph[i].append(j)
                graph[j].append(i)

    answer = [0] * n
    
    for i in range(n):
        visited = [False] * n
        queue = [i]
        cnt = 0

        while queue:
            node = queue.pop(0)
            if visited[node]:
                continue

            visited[node] = True
            cnt += 1

            for neer in graph[node]:
                queue.append(neer)

        answer[i] = cnt

    return answer