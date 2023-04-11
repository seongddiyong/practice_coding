from sys import stdin
from itertools import combinations
input = stdin.readline

n,m = map(int, input().split())
temp = list(map(int, input().split()))
result = 0

for card in combinations(temp,3):
    temp_sum = sum(card)
    if result < temp_sum <= m:
        result = temp_sum

print(result)