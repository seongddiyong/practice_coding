from sys import stdin
input = stdin.readline

n,k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]

m = sorted(m, key = lambda x: (-x[1],-x[2],-x[3]))

rank = [1]
for i in range(n):
    if m[i][0] == k:
        print(rank[i])
        break
    if m[i][1:] == m[i+1][1:]:
        rank.append(rank[i])
    else:
        rank.append(len(rank)+1)
