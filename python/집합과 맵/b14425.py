from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
count = 0
n_string = [input() for _ in range(n)]
for _ in range(m):
    temp = input()
    if temp in n_string:
        count += 1
print(count)