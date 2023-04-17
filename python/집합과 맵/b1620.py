import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pocket = {}
fornum = {}
for i in range(1,n+1):
    name = input().rstrip()
    pocket[i] = name
    fornum[name] = i
for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(pocket[int(q)])
    else:
        print(fornum[q])