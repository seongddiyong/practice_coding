n = int(input())
result = 0
li = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            li[i][j] = 1

for row in li:
    result += row.count(1)
print(result)