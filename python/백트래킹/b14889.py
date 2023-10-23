from sys import stdin
from itertools import combinations
from itertools import permutations
input = stdin.readline
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
person = [i+1 for i in range(n)]
team = list(combinations(person,n//2))
answer = []
mini = 201
for i in range(len(team)//2):
    start = team[i]
    start_score = 0
    link = team[len(team)-1-i]
    link_score = 0
    for x,y in permutations(start,2):
        start_score += g[x-1][y-1]
    for x,y in permutations(link,2):
        link_score += g[x-1][y-1]
    if abs(start_score - link_score) < mini:
        mini = abs(start_score - link_score)
print(mini)