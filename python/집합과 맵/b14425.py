from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
count = 0
n_string = set([input() for _ in range(n)])
for _ in range(m):
    temp = input()
    if temp in n_string:
        count += 1
print(count)

# set 함수를 쓰기 전엔 3712ms가 나왔고 쓰니까 140ms가 나왔다.
# 쓰자..