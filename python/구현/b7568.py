from sys import stdin
input = stdin.readline

n = int(input())
standard = [list(map(int,input().split())) for _ in range(n)]
for w,t in standard:
    rank = 1
    for x,y in standard:
        if w < x and t < y:
            rank += 1
    print(rank, end=" ")